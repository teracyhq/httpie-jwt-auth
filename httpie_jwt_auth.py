"""
JWTAuth auth plugin for HTTPie.
"""

from httpie.plugins import AuthPlugin


__version__ = '0.2.0-dev0'
__author__ = 'hoatle'
__license__ = 'BSD'


class JWTAuth(object):
    """JWTAuth to set the right Authorization header format of JWT"""
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers['Authorization'] = 'Bearer {}'.format(self.token)
        return request


class JWTAuthPlugin(AuthPlugin):
    """Plugin registration"""

    name = 'JWT auth'
    auth_type = 'jwt'
    description = 'Set the right format for JWT auth request'

    def get_auth(self, username, password):
        return JWTAuth(username)
