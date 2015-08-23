"""
JWTAuth auth plugin for HTTPie.
"""

from httpie.plugins import AuthPlugin


__version__ = '0.1.0-dev0'
__author__ = 'hoatle'
__license__ = 'BSD'


class JWTAuth(object):
    """JWTAuth to set the right Authorization header format of JWT"""
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer {}'.format(self.token)
        return r


class JWTAuthPlugin(AuthPlugin):
    """Plugin registration"""

    name = 'JWT auth'
    auth_type = 'jwt'
    description = 'Set the right request for JWT auth format'

    def get_auth(self, username, password):
        return JWTAuth(username)


