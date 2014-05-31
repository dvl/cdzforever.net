# -*- coding: utf-8 -*-

import os

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = int(os.environ.get('DJANGO_DEBUG'))
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEFAULT_FILE_STORAGE = 'libs.storages.S3Storage.S3Storage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'cdzforever'

STATIC_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media'
