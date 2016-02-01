# -*- coding: utf-8 -*-
"""unit test for httpie_jwt_auth"""
import os
from unittest import TestCase

from httpie.plugins import AuthPlugin

from httpie_jwt_auth import JWTAuth, JWTAuthPlugin, __version__, __author__, __license__


class MetaInfoTestCase(TestCase):

    def test_meta_info(self):
        self.assertIsNotNone(__version__)
        self.assertEqual(__author__, 'hoatle')
        self.assertEqual(__license__, 'BSD')


class JWTAuthTestCase(TestCase):

    def test_init(self):
        from httpie_jwt_auth import JWTAuth
        jwt_auth = JWTAuth('token', 'prefix')

        self.assertEqual(jwt_auth.token, 'token')
        self.assertEqual(jwt_auth.auth_prefix, 'prefix')


    def test_call(self):

        class RequestMock(object):
            def __init__(self, headers):
                self.headers = headers

        request = RequestMock({})
        jwt_auth = JWTAuth('token', 'prefix')
        update_request = jwt_auth(request)

        self.assertIsNotNone(update_request.headers['Authorization'])
        self.assertEqual(update_request.headers['Authorization'], 'prefix token')


class JWTAuthPluginTestCase(TestCase):

    def test_instance_type(self):
        jwt_auth_plugin = JWTAuthPlugin()

        self.assertIsInstance(jwt_auth_plugin, AuthPlugin)

    def test_attribute(self):
        self.assertEqual(JWTAuthPlugin.name, 'JWT auth')
        self.assertEqual(JWTAuthPlugin.auth_type, 'jwt')
        self.assertEqual(JWTAuthPlugin.description, 'Set the right format for JWT auth request')

    def test_get_auth_default(self):
        jwt_auth_plugin = JWTAuthPlugin()
        jwt_auth = jwt_auth_plugin.get_auth('token', '')

        self.assertIsNone(os.environ.get('JWT_AUTH_PREFIX'), None)
        self.assertEqual(jwt_auth.token, 'token')
        self.assertEqual(jwt_auth.auth_prefix, 'Bearer')

    def test_get_auth_prefix(self):
        os.environ['JWT_AUTH_PREFIX'] = 'JWT'
        jwt_auth_plugin = JWTAuthPlugin()
        jwt_auth = jwt_auth_plugin.get_auth('token', '')

        self.assertEqual(jwt_auth.token, 'token')
        self.assertEqual(jwt_auth.auth_prefix, 'JWT')
