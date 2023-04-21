from unittest import TestCase

from link_to_term import check_terms_duplicate,load_all_refs


class TestLinkToTerm(TestCase):
    def test_check_terms_duplicate(self):
        all_terms_spelling = {}
        terms = {"a": "b"}
        check_terms_duplicate(all_terms_spelling, terms)
        self.assertEqual(all_terms_spelling, {"A": ["a"]})

        terms = {"a": "b", "A": "b"}
        with self.assertRaises(Exception):
            check_terms_duplicate(all_terms_spelling, terms)
