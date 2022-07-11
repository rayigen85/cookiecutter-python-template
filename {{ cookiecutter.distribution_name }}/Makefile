SPHINX_BUILDDIR ?= _build
SPHINXOPTS ?= "-W"
COMPONENT_NAME = {{ cookiecutter.distribution_name }}
SOURCE_CODE_PATH = src/{{ cookiecutter.package_name }}

.PHONY: black clean clean-backups clean-build clean-docs clean-pyc clean-test coverage\
  coverage-report develop dist docs isort test-flake8 test\
  test-all test-docs test-quick test-style test-types

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "   black                   to blacken (format correctly) the entire codebase."
	@echo "   clean                   to remove all build, test, coverage and Python artifacts."
	@echo "   clean-backups           to remove swap and editor backup artifacts."
	@echo "   clean-build             to remove build artifacts."
	@echo "   clean-docs              to remove sphinx related build artifacts."
	@echo "   clean-pyc               to remove Python file artifacts."
	@echo "   clean-test              to remove test and coverage artifacts."
	@echo "   coverage                to generate a coverage report file."
	@echo "   coverage-report         to check code coverage quickly with the default Python."
	@echo "   develop                 to install (or update) all packages required for development."
	@echo "   dist                    to built the package and upload new global html docs."
	@echo "   docs                    to generate Sphinx HTML documentation, including API docs."
	@echo "   isort                   to run isort on the whole project."
	@echo "   test-manifest           to make sure that source distribution archive and vcs are in sync."
	@echo "   test-flake8             to check style with flake8."
	@echo "   test-isort              to check if imports are ordered as expected."
	@echo "   test-mypy               to perform static type checking with mypy."
	@echo "   test-docs               to run documentation testsuite."
	@echo "   test                    to run just the testsuite quickly with the default Python."
	@echo "   test-all                to run tests on every Python version with tox."
	@echo "   test-quick              to run unitests and select other validations before committing."
	@echo "   test-style              to verify complience with style expectations."
	@echo "   test-tox                to run the entire testsuite fully compartmentalized with tox."

black:
	black $(SOURCE_CODE_PATH)/ tests/

clean: clean-backups clean-build clean-docs clean-pyc clean-test

clean-backups:
	find . -name '*~' -delete
	find . -name '*.orig' -delete
	find . -name '*.swp' -delete

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '__pycache__' -delete

clean-test:
	rm -rf .tox/
	rm -f .coverage
	coverage erase
	rm -rf htmlcov/

coverage:
	coverage run -m pytest $(TEST_ARGS) tests

coverage-report: coverage
	coverage report

develop:
	pip install -U pip
	pip install -U -r requirements/private-repos.pip
	pip install -U -r requirements/dev.pip
	pip install -U -e .

dist: clean test-all
	python3 -m build
	@echo
	ls -lh dist

docs:
	sphinx-apidoc -f -o docs/apidocs/ $(SOURCE_CODE_PATH)/
	$(MAKE) -C docs clean
	$(MAKE) -C docs html SPHINXOPTS=$(SPHINXOPTS)

isort:
	isort setup.py $(SOURCE_CODE_PATH)/ tests/

test-manifest:
	check-manifest -v

test-flake8:
	flake8 $(SOURCE_CODE_PATH)/ tests/

test-isort:
	isort --check-only --verbose $(SOURCE_CODE_PATH)/ tests/

test-black:
	black --check $(SOURCE_CODE_PATH)/ tests/

test-mypy:
	mypy $(SOURCE_CODE_PATH)/

test-docs: docs
	doc8 docs/

test:
	py.test  tests/

test-all: test-style coverage-report test-types test-manifest test-docs test-mypy

test-quick: test test-style test-types

test-style: test-black test-flake8 test-isort

test-tox:
	tox
