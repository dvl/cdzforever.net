# -*- coding: utf-8 -*-

import os

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

DEBUG = os.environ['DJANGO_DEBUG']
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

STATIC_ROOT = 'staticfiles'
MEDIA_ROOT = 'media' 
