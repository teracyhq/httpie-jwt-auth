resolve:
	pip install -r requirements.txt --upgrade

check-style:
	flake8 --max-complexity 12 . || exit 0
	pylint --rcfile .pylintrc *.py **/*.py || exit 0

test-clean:
	coverage erase

test-unit:
	coverage run --branch --source=. `which nosetests` -v --exe

test: | test-clean test-unit

report-coverage:
	coverage report --omit=tests/*,setup.py

.DEFAULT_GOAL := resolve

.PHONY: resolve, check-style, report-coverage, test-clean, test-unit, test
