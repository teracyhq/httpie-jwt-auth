httpie-jwt-auth |travis build status|_ |coveralls status|_ |pypi status|_
==========================================================================

`JWTAuth (JSON Web Tokens) <https://github.com/teracyhq/httpie-jwt-auth>`_ auth plugin for
`HTTPie <https://github.com/jkbr/httpie>`_.


Installation
------------

- Latest stable version:

..  code-block:: bash

    $ pip install -U httpie-jwt-auth

- Latest developing version:

..  code-block:: bash

    $ pip install -U https://github.com/teracyhq/httpie-jwt-auth/archive/develop.zip


Usage
-----

..  code-block:: bash

    $ http --auth-type=jwt --auth='<token>:' example.org

Note: Remember to add `:` after the token.


Contributing
------------

Please create pull requests to the `develop` branch by following http://dev.teracy.org/docs/workflow.html


FAQs
----

#.  How to load JWT token from a file?

    ..  code-block:: bash

        $ http --auth-type=jwt --auth=$(cat mytoken.txt): example.org

    See: https://github.com/teracyhq/httpie-jwt-auth/issues/4

#.  How to use auth prefix other than default `Bearer`, for example `Token_Prefix` instead?

    You could use environment variable to specify `JWT_AUTH_PREFIX`.

    ..  code-block:: bash

        $ export JWT_AUTH_PREFIX=Token_Prefix

    and it should work:

    .. code-block:: bash

        $ http teracy.com --auth-type=jwt --auth=abc: -v

        GET / HTTP/1.1
        Accept: */*
        Accept-Encoding: gzip, deflate
        Authorization: Token_Prefix abc
        Connection: keep-alive
        Host: teracy.com
        User-Agent: HTTPie/0.9.2

Discussions
-----------

Join us:

- https://groups.google.com/forum/#!forum/teracy

- https://www.facebook.com/groups/teracy

Get our news:

- https://www.facebook.com/teracyhq

- https://twitter.com/teracyhq


Author and contributors
-----------------------

See more details at `AUTHORS.md` and `CONTRIBUTORS.md` files.


License
-------

BSD License

::

  Copyright (c) Teracy, Inc. and individual contributors.
  All rights reserved.

  Redistribution and use in source and binary forms, with or without modification,
  are permitted provided that the following conditions are met:

      1. Redistributions of source code must retain the above copyright notice,
         this list of conditions and the following disclaimer.

      2. Redistributions in binary form must reproduce the above copyright
         notice, this list of conditions and the following disclaimer in the
         documentation and/or other materials provided with the distribution.

      3. Neither the name of Teracy, Inc. nor the names of its contributors may be used
         to endorse or promote products derived from this software without
         specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

.. |travis build status| image:: https://travis-ci.org/teracyhq/httpie-jwt-auth.png?branch=develop
.. _travis build status: https://travis-ci.org/teracyhq/httpie-jwt-auth

.. |coveralls status| image:: https://coveralls.io/repos/github/teracyhq/httpie-jwt-auth/badge.svg?branch=develop
.. _coveralls status: https://coveralls.io/github/teracyhq/httpie-jwt-auth?branch=develop

.. |pypi status| image:: https://badge.fury.io/py/httpie-jwt-auth.svg
.. _pypi status: https://badge.fury.io/py/httpie-jwt-auth
