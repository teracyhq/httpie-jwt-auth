resolve:
	pip install -r requirements-dev.txt --upgrade

check-style:
	flake8 --max-complexity 12 . || exit 0
	pylint --rcfile .pylintrc *.py **/*.py || exit 0

test:
	pytest --cov=.

.DEFAULT_GOAL := resolve

.PHONY: resolve, check-style, test
