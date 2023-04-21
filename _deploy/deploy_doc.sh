set -e;

echo ">> prepare..."
echo "TMP_NAME: ${TMP_NAME}"
echo "TEAM_NAME: ${TEAM_NAME}"

rm -rf /data/rubbish/*;
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX);
work_dir=$(pwd);

tar -xzf ${TMP_NAME}.tar.gz -C ${tmp_dir};
cd ${tmp_dir};

echo ">> building..."
# echo "$(env)"
git submodule update --init --recursive;
docker run --rm -v $(pwd):/app -w /app ppcelery/kipp:20220606 ./_scripts/link_to_term.py --dir=./content --write;
docker run --rm -v $(pwd):/app -w /app klakegg/hugo:0.93.2-debian --minify;
docker run --rm -v $(pwd):/app -w /app --entrypoint /bin/chmod ppcelery/kipp:20220606 -R 777 /app;

echo ">> updating..."
mkdir -p /var/www/doc/${TEAM_NAME} 2>/dev/null || true;
mv /var/www/doc/${TEAM_NAME}/* /data/rubbish 2>/dev/null || true;
mv ./public/* /var/www/doc/${TEAM_NAME}/.;

echo ">> cleanning..."
cd ${work_dir};
mv ${TMP_NAME}.tar.gz /data/rubbish/.;
mv ${TMP_NAME}.sh /data/rubbish/.;
mv ${tmp_dir} /data/rubbish 2>/dev/null || true;
rm -rf /data/rubbish/*;
