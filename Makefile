.PHONY: install
install:
	git submodule deinit -f themes/hugo-book
	git pull && git submodule init && git submodule update && git submodule status

.PHONY: run
run:
	rm -rf ./public
	hugo server --bind=0.0.0.0 --port=21314 --minify

.PHONY: build
build:
	rm -rf ./public
	hugo --minify

# .PHONY: update
# update:
# 	git remote add upstream git@git.basebit.me:xego/doc-template.git 2>/dev/null || true
# 	git fetch upstream
# 	git merge upstream/master

# deploy:
# 	make build
# 	tar -czf public.tar.gz public
# 	# scp public.tar.gz linode:/var/www/private/basebit/xss/.
# 	# rm -rf ./public.tar.gz
# 	# ssh linode "cd /var/www/private/basebit/xss/ && tar -xzf public.tar.gz"
# 	scp public.tar.gz xego:/var/www/xss/.
# 	rm -rf ./public.tar.gz
# 	ssh xego "cd /var/www/xss && tar -xzf public.tar.gz"

.PHONY: test
test:
	pytest -v ./_scripts

.PHONY: lint
lint:
	pip install kipp
	python ./_scripts/link_to_term.py --dir=./content

.PHONY: auto-terms
auto-terms:
	python ./_scripts/link_to_term.py --dir=./content --write
