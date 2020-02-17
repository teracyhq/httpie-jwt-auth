# -*- coding: utf-8 -*-

"""
JWTAuth auth plugin for HTTPie.
"""
import os

from httpie.plugins import AuthPlugin

__version__ = '0.4.0'
__author__ = 'hoatle'
__license__ = 'BSD'


class JWTAuth(object):
    """JWTAuth to set the right Authorization header format of JWT"""

    def __init__(self, token, auth_header, auth_prefix):
        self.token = token
        self.auth_header = auth_header
        self.auth_prefix = auth_prefix

    def __call__(self, request):
        request.headers[self.auth_header] = '{0} {1}'.format(self.auth_prefix, self.token)
        return request


class JWTAuthPlugin(AuthPlugin):
    """Plugin registration"""

    name = 'JWT auth'
    auth_type = 'jwt'
    description = 'Set the right format for JWT auth request'
    auth_require = False
    prompt_password = False

    def get_auth(self, username=None, password=None):
        auth_header = os.environ.get('JWT_AUTH_HEADER', 'Authorization')
        auth_prefix = os.environ.get('JWT_AUTH_PREFIX', 'Bearer')
        env_token = os.environ.get('JWT_AUTH_TOKEN')
        if username is None:
            username = env_token
        if username is None:
            raise Exception('--auth or JWT_AUTH_TOKEN required error')
        return JWTAuth(username, auth_header, auth_prefix)
