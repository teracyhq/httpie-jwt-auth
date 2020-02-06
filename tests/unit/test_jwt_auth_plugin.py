# -*- coding: utf-8 -*-
"""unit test for httpie_jwt_auth:JWTAuthPlugin"""
import os

from httpie.plugins import AuthPlugin

from httpie_jwt_auth import JWTAuthPlugin


def test_instance_type():
    jwt_auth_plugin = JWTAuthPlugin()

    assert isinstance(jwt_auth_plugin, AuthPlugin)


def test_attribute():
    assert JWTAuthPlugin.name == 'JWT auth'
    assert JWTAuthPlugin.auth_type == 'jwt'
    assert JWTAuthPlugin.description == 'Set the right format for JWT auth request'
    assert JWTAuthPlugin.auth_require is False
    assert JWTAuthPlugin.prompt_password is False


def test_get_auth_default():
    jwt_auth_plugin = JWTAuthPlugin()
    jwt_auth = jwt_auth_plugin.get_auth('token', '')

    assert os.environ.get('JWT_AUTH_PREFIX') is None
    assert jwt_auth.token == 'token'
    assert jwt_auth.auth_prefix == 'Bearer'


def test_get_auth_prefix():
    os.environ['JWT_AUTH_PREFIX'] = 'JWT'
    jwt_auth_plugin = JWTAuthPlugin()
    jwt_auth = jwt_auth_plugin.get_auth('token', '')

    assert jwt_auth.token == 'token'
    assert jwt_auth.auth_prefix == 'JWT'
    del os.environ['JWT_AUTH_PREFIX']


def test_get_auth_header():
    os.environ['JWT_AUTH_HEADER'] = 'X-Foobar-Authorization'
    jwt_auth_plugin = JWTAuthPlugin()
    jwt_auth = jwt_auth_plugin.get_auth('token', '')

    assert jwt_auth.token == 'token'
    assert jwt_auth.auth_header == 'X-Foobar-Authorization'
    del os.environ['JWT_AUTH_HEADER']


def test_get_auth_prefix_and_token():
    os.environ['JWT_AUTH_PREFIX'] = 'JWT'
    os.environ['JWT_AUTH_TOKEN'] = 'secret'
    jwt_auth_plugin = JWTAuthPlugin()
    jwt_auth = jwt_auth_plugin.get_auth()

    assert jwt_auth.token == 'secret'
    assert jwt_auth.auth_prefix == 'JWT'
    del os.environ['JWT_AUTH_PREFIX']
    del os.environ['JWT_AUTH_TOKEN']


def test_get_auth_none():
    jwt_auth_plugin = JWTAuthPlugin()
    try:
        jwt_auth_plugin.get_auth()
    except Exception as ex:
        assert str(ex) == '--auth or JWT_AUTH_TOKEN required error'
