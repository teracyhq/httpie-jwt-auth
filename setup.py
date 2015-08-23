from setuptools import setup

try:
    import multiprocessing
except ImportError:
    pass

import httpie_jwt_auth

setup(
    name='httpie-jwt-auth',
    description='JWTAuth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version=httpie_jwt_auth.__version__,
    author='hoatle',
    author_email='hoatle@teracy.com',
    license='BSD',
    url='https://github.com/teracyhq/httpie-jwt-auth',
    download_url='https://github.com/teracyhq/httpie-jwt-auth',
    py_modules=['httpie_jwt_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_jwt_auth = httpie_jwt_auth:JWTAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
