Release Process
===============

do the following steps to proceed the release.

Next iteration
--------------

Update for the next iteration for the develop branch:

- update ``__version__`` on the ``httpie_jwt_auth.py`` file 


CHANGELOG.rst
-------------

- update changelog


httpie_jwt_auth.py
------------------

- update ``__version__`` (for both the develop branch and releases branches)


Upload the tagged version to PyPI
---------------------------------

..  code-block:: bash

    $ git checkout vX.X.X
    $ python setup.py sdist bdist_wheel --universal
    $ twine upload dist/*

Ref:

- http://python-packaging-user-guide.readthedocs.io/distributing/

- https://github.com/pypa/twine
