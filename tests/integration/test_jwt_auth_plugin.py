# -*- coding: utf-8 -*-
"""integration test for httpie_jwt_auth:JWTAuthPlugin"""
import os

from httpie.plugins import plugin_manager

from httpie_jwt_auth import JWTAuthPlugin
from .utils import http, HTTP_OK

plugin_manager.register(JWTAuthPlugin)


def test_required(httpbin):
    """$ http [url] --auth-type=jwt => --auth or JWT_AUTH_TOKEN required error"""
    try:
        r = http(
            httpbin.url + '/headers',
            '--auth-type',
            'jwt'
        )
    # TODO(hoatle): handle this
    # assert r.exit_status == 1
    # assert '--auth or JWT_AUTH_TOKEN required error' in r.stdout or r.stderr
    # basically print error with the same behavior like: `--auth required error`
    except Exception as ex:
        assert '--auth or JWT_AUTH_TOKEN required error' in str(ex)


def test_colon_character(httpbin):
    """
    $ http [url] --auth-type=jwt --auth=abc:
    => the right Authorization request header with default token prefix (Bearer)
    This is compatible behavior with httpie-jwt-auth v0.2.1 and below
    """
    r = http(
        httpbin.url + '/headers',
        '--auth-type',
        'jwt',
        '--auth',
        'abc:'
    )
    assert HTTP_OK in r
    assert r.json['headers']['Authorization'] == 'Bearer abc'


def test_default_prefix(httpbin):
    """
    $ http [url] --auth-type=jwt --auth=abc
    => the right Authorization request header with default token prefix (Bearer)

    this requires HTTPie version 0.9.7 and above
    """
    r = http(
        httpbin.url + '/headers',
        '--auth-type',
        'jwt',
        '--auth',
        'abc'
    )
    assert HTTP_OK in r
    assert r.json['headers']['Authorization'] == 'Bearer abc'


def test_specified_env_token(httpbin):
    """
    sometimes, putting the token on the command line is not preferred, we should support environment variable
    $ export JWT_AUTH_TOKEN=abc
    $ http [url] --auth-type=jwt
    """
    os.environ['JWT_AUTH_TOKEN'] = 'secret'
    r = http(
        '--auth-type',
        'jwt',
        httpbin.url + '/headers'
    )
    assert HTTP_OK in r
    assert r.json['headers']['Authorization'] == 'Bearer secret'
    # cleanup
    del os.environ['JWT_AUTH_TOKEN']


def test_env_token_and_auth(httpbin):
    """
    set both JWT_AUTH_TOKEN and --auth -> --auth has higher priority
    """
    os.environ['JWT_AUTH_TOKEN'] = 'secret'
    r = http(
        '--auth-type',
        'jwt',
        '--auth',
        'abc',
        httpbin.url + '/headers'
    )
    assert HTTP_OK in r
    assert r.json['headers']['Authorization'] == 'Bearer abc'
    # cleanup
    del os.environ['JWT_AUTH_TOKEN']


def test_specified_env_prefix(httpbin):
    """
    $ JWT_AUTH_PREFIX=JWT http --auth-type=jwt --auth="xyz" [url]
    => the right Authorization request header with defined token prefix (JWT)
    """
    os.environ['JWT_AUTH_PREFIX'] = 'JWT'
    assert os.environ.get('JWT_AUTH_PREFIX') == 'JWT'
    r = http(
        '--auth-type',
        'jwt',
        '--auth',
        'xyz',
        httpbin.url + '/headers'
    )
    assert HTTP_OK in r
    assert r.json['headers']['Authorization'] == 'JWT xyz'
    # cleanup
    del os.environ['JWT_AUTH_PREFIX']


def test_specified_env_header(httpbin):
    """
    $ JWT_AUTH_HEADER=X-Foobar-Authorization http --auth-type=jwt --auth="xyz" [url]
    => the right X-Foobar-Authorization request header
    """
    os.environ['JWT_AUTH_HEADER'] = 'X-Foobar-Authorization'
    assert os.environ.get('JWT_AUTH_HEADER') == 'X-Foobar-Authorization'
    r = http(
        '--auth-type',
        'jwt',
        '--auth',
        'xyz',
        httpbin.url + '/headers'
    )
    assert HTTP_OK in r
    assert r.json['headers']['X-Foobar-Authorization'] == 'Bearer xyz'
    # cleanup
    del os.environ['JWT_AUTH_HEADER']


def test_specified_both_env_prefix_and_env_token(httpbin):
    os.environ['JWT_AUTH_PREFIX'] = 'JWT'
    os.environ['JWT_AUTH_TOKEN'] = 'secret'
    r = http(
        '--auth-type',
        'jwt',
        httpbin.url + '/headers'
    )
    assert HTTP_OK in r
    assert r.json['headers']['Authorization'] == 'JWT secret'
    # cleanup
    del os.environ['JWT_AUTH_PREFIX']
    del os.environ['JWT_AUTH_TOKEN']


def test_specified_env_header_and_env_prefix_and_env_token(httpbin):
    os.environ['JWT_AUTH_HEADER'] = 'X-Foobar-Authorization'
    os.environ['JWT_AUTH_PREFIX'] = 'JWT'
    os.environ['JWT_AUTH_TOKEN'] = 'secret'
    r = http(
        '--auth-type',
        'jwt',
        httpbin.url + '/headers'
    )
    assert HTTP_OK in r
    assert r.json['headers']['X-Foobar-Authorization'] == 'JWT secret'
    # cleanup
    del os.environ['JWT_AUTH_HEADER']
    del os.environ['JWT_AUTH_PREFIX']
    del os.environ['JWT_AUTH_TOKEN']


# TODO(hoatle): implement this
# def test_specified_option_prefix(httpbin):
#     """
#     $ http --auth-type="jwt" --auth="abc" --auth-prefix="JWT" [url]
#     => the right Authorization request header with defined token prefix (JWT)
#     use this way when you have to switch with different jwt auth prefix
#     this requires HTTPie version 0.9.7 and above
#     """
#     r = http(
#         httpbin.url + '/headers',
#         '--auth-type',
#         'jwt',
#         '--auth',
#         'xyz',
#     )
#     assert HTTP_OK in r
#     assert r.json['headers']['Authorization'] == 'JWT xyz'
