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
