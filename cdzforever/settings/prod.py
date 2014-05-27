# -*- coding: utf-8 -*-

import os

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = os.getenv('DJANGO_DEBUG', False)
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'
