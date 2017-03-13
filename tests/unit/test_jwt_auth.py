# -*- coding: utf-8 -*-
"""unit test for httpie_jwt_auth:JWTAuth"""

from httpie_jwt_auth import JWTAuth, __version__, __author__, __license__


def test_meta_info():
    assert __version__ is not None
    assert __author__ == 'hoatle'
    assert __license__ == 'BSD'


def test_init():
    from httpie_jwt_auth import JWTAuth
    jwt_auth = JWTAuth('token', 'prefix')

    assert jwt_auth.token == 'token'
    assert jwt_auth.auth_prefix == 'prefix'


def test_call():

    class RequestMock(object):
        def __init__(self, headers):
            self.headers = headers

    request = RequestMock({})
    jwt_auth = JWTAuth('token', 'prefix')
    updated_request = jwt_auth(request)

    assert updated_request.headers['Authorization'] is not None
    assert updated_request.headers['Authorization'] == 'prefix token'
