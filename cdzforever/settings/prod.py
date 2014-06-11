# -*- coding: utf-8 -*-

import os

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_API_SECRET')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = int(os.environ.get('DJANGO_DEBUG'))
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

STATICFILES_STORAGE = 'apps.core.storage.S3PipelineStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'
