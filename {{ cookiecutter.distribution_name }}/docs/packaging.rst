SemVer
=========

``{{ cookiecutter.distribution_name }}`` follows the `semantic versioning
<https://semver.org>`_ scheme.  We provide a compliant ``setup.py`` which
contains all the meta information relevant to users of
``{{ cookiecutter.distribution_name }}``.
If you stumble upon any incompatibilities or dependency issue please let us
know.


About requirements/\*.pip
-------------------------
We do fully follow Donald Stuffts `argument
<https://caremad.io/2013/07/setup-vs-requirement/>`_ that information given in
``setup.py`` is of fundamentally different nature than what may be located
under ``requirements.txt`` (Additional comments can be found in the `packaging
guide
<http://python-packaging-user-guide.readthedocs.org/en/latest/requirements/>`_
and with `Hynek Schlawack
<https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/>`_).
As far as packaging goes ``setup.py`` is authoritative. We provide a set of
specific environments under ``requirements/*`` that mainly developers and 3rd
parties may find useful. This way we can easily enable contributers to get a
suitable ``virtualenv`` running or specify our test environment in one central
location.
