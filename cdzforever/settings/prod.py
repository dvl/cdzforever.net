# -*- coding: utf-8 -*-

import os

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

RQ_QUEUES = {
    'high': {
        'USE_REDIS_CACHE': os.environ.get('REDISTOGO_URL', 'redis://localhost:6379'),
    },
    'default': {
        'USE_REDIS_CACHE': os.environ.get('REDISTOGO_URL', 'redis://localhost:6379'),
    },
    'low': {
        'USE_REDIS_CACHE': os.environ.get('REDISTOGO_URL', 'redis://localhost:6379'),
    },
}

ALLOWED_HOSTS = ['*']

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_API_SECRET')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = INSTALLED_APPS + (
    'storages',
)

DEBUG = int(os.environ.get('DJANGO_DEBUG'))
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'

