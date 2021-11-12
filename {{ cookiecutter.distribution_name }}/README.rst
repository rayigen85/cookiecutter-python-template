{{ cookiecutter.distribution_name }}
====================================

{{ cookiecutter.description_short }}

Requirement for the production environment
------------------------------------------
- Python 3.6

How to create a development environment
---------------------------------------

#. Create a new `venv`::

   $ python3 -m venv <VENV_NAME>

#. Activate new `venv`::

   $ source <VENV_NAME>/bin/activate

#. Install all packages required for a proper development runtime env::

   $ make develop

How to run the test suite
-------------------------

The complete test suite can be triggered with the following command, assuming that the
development environment has been properly created as explained earlier.::

   $ make test-tox

Using ``make help`` a multitude of additional `make targets` can be listed. Those allow
for running highly granular subsets of tests. For a quick and dirty testing during
active feature development, the following may be particularilly usefull.::

   $ make test-quick

.. important::
   For several central ``make targets`` it is required to clone repositories of other
   NWA components. In order to avoid being prompted for passord of the required ssh
   key it is adviseable to make sure it is added to a running ``ssh-agent``.::

   $ ssh-agent
   $ …
   $ ssh-add
