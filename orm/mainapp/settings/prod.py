from .base import *
import os

DEBUG = False

if 'DYNO' in os.environ:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    os.environ['HTTPS'] = "on"

ALLOWED_HOSTS = [
    "pylfolio.ovh"
]
