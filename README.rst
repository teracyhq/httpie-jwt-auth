httpie-jwt-auth
===============

`JWTAuth (JSON Web Tokens) <https://github.com/teracyhq/httpie_jwt_auth>`_ auth plugin for
`HTTPie <https://github.com/jkbr/httpie>`_.


Installation
------------

..  code-block:: bash

    $ pip install httpie-jwt-auth


Usage
-----

..  code-block:: bash

    $ http --auth-type=jwt --auth='<token>:' example.org

Note: Remember to add `:` after the token.


FAQs
----

#. How to load JWT token from a file?

    ..  code-block:: bash

        $ http --auth-type=jwt --auth=$(cat mytoken.txt): example.org

    See: https://github.com/teracyhq/httpie-jwt-auth/issues/4


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
