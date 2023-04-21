import codecs
import glob
import os
import re
from textwrap import dedent
from typing import Dict, Generator, List

from kipp.options import options as opt
from kipp.utils import setup_logger

logger = setup_logger("doc_linker")


REGEX_TERMS: re.Pattern = re.compile(
    r"[^!]\[(?P<term>[^\]]+)\]\((?P<link>[^\)]+)\)", flags=re.M
)
REGEX_BRACKET = re.compile(
    r"(?:\[[^\]]+\])|(?:\([^\)]+\))|(?:`[^`]+`)|(?:\{[^\}]+\})", flags=re.M
)

IGNORE_TERMS = set(
    [
        "More...",
    ]
)


def main():
    parse_args()
    logger.info(f"scan dir {opt.dir}...")

    replace_refs()
    check_links()


REGEX_REFS_FORMAT = lambda ref_id: rf"(^| )\({ref_id}\)=($| )"
REGEX_REFS = re.compile(r"(?:^| )\((?P<ref_id>[^\)]+)\)=(?:$| )", flags=re.M)
REGEX_LINK_TO_REF = re.compile(r"\[[^\]]+\]\(@(?P<ref_id>[^\)]+)\)", flags=re.M)


def replace_refs():
    all_refs_id_to_link: Dict[str, str] = {}
    for fpath in list_all_files(opt.dir):
        load_and_replace_refs(all_refs_id_to_link, opt.dir, fpath)

    for fpath in list_all_files(opt.dir):
        replace_links_to_ref(all_refs_id_to_link, fpath)


def replace_links_to_ref(all_refs_id_to_link: Dict[str, str], fpath: str):
    """replace all refs by link"""
    with codecs.open(fpath, "r", "utf8") as fp:
        file_cnt = fp.read()

    for matched in REGEX_LINK_TO_REF.finditer(file_cnt):
        ref_id = matched.group("ref_id")
        if ref_id not in all_refs_id_to_link:
            raise Exception(f"unknown ref_id `{ref_id}` in {fpath}")

        new_text = matched.group(0).replace(f"@{ref_id}", all_refs_id_to_link[ref_id])
        file_cnt = file_cnt.replace(matched.group(0), new_text)

    if opt.write:
        with codecs.open(fpath, "w", "utf8") as fp:
            fp.write(file_cnt)


def load_and_replace_refs(
    all_refs_id_to_link: Dict[str, str], root_path: str, fpath: str
):
    """Load all refs from file

    refs format like: ` (<ref_uuid>)= `

    Args:
        - all_refs_id_to_link: all refs id to link
        - root_path: root directory path, will used to generate relative url path of each file
        - fpath: markdown file path
    """
    with codecs.open(fpath, "r", "utf8") as fp:
        file_cnt = fp.read()

    rel_url = fpath.removeprefix(root_path).removesuffix(".md").removesuffix("/_index")
    for matched in REGEX_REFS.finditer(file_cnt):
        ref_id = matched.group("ref_id")
        if ref_id in all_refs_id_to_link:
            raise Exception(f"duplicate ref id: `({ref_id})=` in {fpath}")

        all_refs_id_to_link[ref_id] = f'{{{{% ref "{rel_url}#{ref_id}" %}}}}'
        file_cnt = re.sub(
            REGEX_REFS_FORMAT(ref_id),
            rf'\1<div id="{ref_id}"></div>\2',
            file_cnt,
            flags=re.M,
        )

    if opt.write:
        with codecs.open(fpath, "w", "utf8") as fp:
            fp.write(file_cnt)


def check_links():
    """check markdown links like `[xx](yy)` which links to `/terms`"""

    all_terms_spelling: Dict[str, List[str]] = {}
    all_term_to_link: Dict[str, str] = {}
    all_link_to_term: Dict[str, str] = {}

    for fpath in list_all_files(opt.dir):
        logger.info(f"scan file {fpath}")

        with codecs.open(fpath, "r", "utf8") as fp:
            file_cnt = fp.read()

        terms = collect_terms(file_cnt)
        # check if there are differnet links related to the same term
        check_and_merge_dict(all_term_to_link, terms, exception=False)
        # check if there are differnet terms related to the same link
        check_and_merge_dict(all_link_to_term, {v: k for k, v in terms.items()})
        # check if there are duplicate terms in the same spelling
        check_terms_duplicate(all_terms_spelling, terms)
        # auto replace all terms with links
        # if opt.write:
        #     auto_link(fpath, all_term_to_link)


def auto_link(fpath: str, all_term_to_link: Dict[str, str]):
    with codecs.open(fpath, "r", "utf8") as fp:
        file_cnt = fp.readlines()

    is_in_header_block = False
    for i, line in enumerate(file_cnt):
        if is_in_header_block:
            if line.startswith("---"):
                is_in_header_block = False

            continue

        if line.startswith("---"):
            is_in_header_block = True
            continue

        if line.strip().startswith("#"):
            continue

        all_brackets: List[tuple[int, int]] = []
        for matched in REGEX_BRACKET.finditer(line):
            all_brackets.append(matched.span())

        is_in_brackets = lambda idx: any(
            idx >= start and idx < end for start, end in all_brackets
        )

        for term, link in all_term_to_link.items():
            for matched in re.finditer(rf"{term}", line):
                if is_in_brackets(matched.start()):
                    continue

                start, end = matched.span()
                # if term is not surrounded by space,
                # we print warning to notify user without replace it
                if (start != 0 and line[start - 1] != " ") or (
                    end != len(line) and line[end] != " "
                ):
                    logger.warning(
                        dedent(
                            f"""
                        {fpath}:{i+1}
                            `{term}` is not surrounded by space
                            may link to: {link}
                        """
                        )
                    )
                    continue

                line = line[:start] + f"[{term}]({link})" + line[end:]
                break

        file_cnt[i] = line

    with codecs.open(fpath, "w", "utf8") as fp:
        fp.write("".join(file_cnt))


def check_terms_duplicate(
    all_terms_spelling: Dict[str, List[str]], terms: Dict[str, str]
):
    """check if there are duplicate terms in different spelling"""
    for term in terms:
        if term.upper() not in all_terms_spelling:
            all_terms_spelling[term.upper()] = [term]
            continue

        # term.upper() in all_terms_uppercase but term not in,
        # means duplicate by different spelling
        another_spelling = all_terms_spelling[term.upper()][0]
        if another_spelling.upper() != term.upper():  # case insensitive
            raise Exception(
                dedent(
                    f"""
            `{term}` has multiple spellings:
            1. `{term}`
            2. `{another_spelling}`
            """
                )
            )


def check_and_merge_dict(to: Dict[str, str], fr: Dict[str, str], exception=False):
    """merge `fr` into `to`

    if value in fr is not as same as value in to, raise exception
    """
    for k, v in fr.items():
        if k not in to:
            to[k] = v
            continue

        if to[k] != v:
            err_msg = dedent(
                f"""
                `{k}` relates to multiple values:
                    1. {to[k]}
                    2. {v}
                    """
            )
            if exception:
                raise Exception(err_msg)
            else:
                logger.warning(err_msg)


def collect_terms(content: str) -> Dict[str, str]:
    """collect terms and links from a markdown file by regex"""
    result = {}
    for term, link in REGEX_TERMS.findall(content):
        if term.strip() == "":
            raise Exception(f"empty term in {link}")

        if term in IGNORE_TERMS:
            continue

        # only deal with in-site link
        if not link.startswith('{{% ref "/terms#'):
            continue

        if term not in result:
            result[term] = link
            continue

        if result[term] != link:
            msg = dedent(
                f"""
            `{term}` has multiple links:
                1. {result[term]}
                2. {link}"""
            )
            # raise Exception(msg)
            logger.warning(msg)

    return result


def list_all_files(dir_path: str) -> Generator[str, None, None]:
    """list all files in a directory recursively"""
    yield from glob.iglob(os.path.join(dir_path, "**", "*.md"), recursive=True)


def parse_args():
    """parse command line arguments"""
    opt.add_argument("--dir", default="./content")
    opt.add_argument("--ext", default="md")
    opt.add_argument("--write", default=False, action="store_true")
    opt.parse_args()

    opt.set_option("dir", opt.dir.rstrip("/"))
    if not opt.dir.startswith("/"):
        opt.dir = os.path.join(os.getcwd(), opt.dir.removeprefix("./"))


if __name__ == "__main__":
    main()
