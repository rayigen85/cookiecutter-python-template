SPHINX_BUILDDIR ?= _build
SPHINXOPTS ?= "-W"
COMPONENT_NAME = {{ cookiecutter.distribution_name }}
SOURCE_CODE_PATH = src/{{ cookiecutter.package_name }}
HTML_INDEX_FILE_PATH = data/index.html
HTML_DEPLOYMENT_BASE_DIR ?= /var/www/html/nwa
HTML_DEPLOYMENT_GLOBAL_BASE_DIR = $(HTML_DEPLOYMENT_BASE_DIR)/global
HTML_DEPLOYMENT_USER_BASE_DIR = $(HTML_DEPLOYMENT_BASE_DIR)/$(USER)
HTML_DEPLOYMENT_GLOBAL_COMPONENT_DIR = $(HTML_DEPLOYMENT_GLOBAL_BASE_DIR)/$(COMPONENT_NAME)
HTML_DEPLOYMENT_USER_COMPONENT_DIR = $(HTML_DEPLOYMENT_USER_BASE_DIR)/$(COMPONENT_NAME)
DOCS_HTML_DEPLOYMENT_LOCATION_GLOBAL = $(HTML_DEPLOYMENT_GLOBAL_COMPONENT_DIR)/docs
DOCS_HTML_DEPLOYMENT_LOCATION_USER = $(HTML_DEPLOYMENT_USER_COMPONENT_DIR)/docs
COVERAGE_BUILDDIR = htmlcov
COVERAGE_HTML_DEPLOYMENT_LOCATION_GLOBAL = $(HTML_DEPLOYMENT_GLOBAL_COMPONENT_DIR)/coverage
COVERAGE_HTML_DEPLOYMENT_LOCATION_USER = $(HTML_DEPLOYMENT_USER_COMPONENT_DIR)/coverage

PRE_COMMIT_HOOK_TYPES = pre-commit pre-merge-commit pre-push prepare-commit-msg commit-msg post-checkout post-commit post-merge post-rewrite
PRE_COMMIT_HOOK_TYPES_ARGUMENT_LIST = $(foreach type,$(PRE_COMMIT_HOOK_TYPES),--hook-type $(type))

.PHONY: black clean clean-backups clean-build clean-docs clean-pyc clean-test coverage\
  coverage-report develop deploy-coverage deploy-docs dist docs isort test-flake8 test\
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
	@echo "   deploy-coverage         to generate a html coverage report and deploy it to the user specific webroot."
	@echo "   deploy-coverage-global  to generate a html coverage report and deploy it to the global  webroot."
	@echo "   deploy-docs             to generate documentation and deploy it to the user specific webroot."
	@echo "   deploy-docs-global      to generate documentation and deploy it to the global webroot."
	@echo "   deploy-html             to deploy all html artefacts to user specific webroot."
	@echo "   deploy-html-global      to deploy all html artefacts to global webroot."
	@echo "   install-git-hooks       to install a set of provided git hooks to the repository."
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
	pre-commit install $(PRE_COMMIT_HOOK_TYPES_ARGUMENT_LIST)

deploy-coverage: coverage
	coverage html
	mkdir -p $(COVERAGE_HTML_DEPLOYMENT_LOCATION_USER)
	rm -rf $(COVERAGE_HTML_DEPLOYMENT_LOCATION_USER)/*
	cp -r $(COVERAGE_BUILDDIR)/* $(COVERAGE_HTML_DEPLOYMENT_LOCATION_USER)

deploy-coverage-global: coverage
	coverage html
	mkdir -p $(COVERAGE_HTML_DEPLOYMENT_LOCATION_GLOBAL)
	rm -rf $(COVERAGE_HTML_DEPLOYMENT_LOCATION_GLOBAL)/*
	cp -r $(COVERAGE_BUILDDIR)/* $(COVERAGE_HTML_DEPLOYMENT_LOCATION_GLOBAL)

deploy-docs: docs
	mkdir -p $(DOCS_HTML_DEPLOYMENT_LOCATION_USER)
	rm -rf $(DOCS_HTML_DEPLOYMENT_LOCATION_USER)/*
	cp -r docs/$(SPHINX_BUILDDIR)/html/* $(DOCS_HTML_DEPLOYMENT_LOCATION_USER)

deploy-docs-global: docs
	mkdir -p $(DOCS_HTML_DEPLOYMENT_LOCATION_GLOBAL)
	rm -rf $(DOCS_HTML_DEPLOYMENT_LOCATION_GLOBAL)/*
	cp -r docs/$(SPHINX_BUILDDIR)/html/* $(DOCS_HTML_DEPLOYMENT_LOCATION_GLOBAL)

deploy-html: deploy-docs deploy-coverage
	cp $(HTML_INDEX_FILE_PATH) $(HTML_DEPLOYMENT_USER_COMPONENT_DIR)

deploy-html-global: deploy-docs-global deploy-coverage-global
	cp $(HTML_INDEX_FILE_PATH) $(HTML_DEPLOYMENT_GLOBAL_COMPONENT_DIR)

install-git-hooks:
	pre-commit install $(PRE_COMMIT_HOOK_TYPES_ARGUMENT_LIST)

dist: clean test-all deploy-html-global
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
