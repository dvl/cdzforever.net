# -*- coding: utf-8 -*-

import os

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
