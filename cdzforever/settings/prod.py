# -*- coding: utf-8 -*-

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'u94[9t8Zm<eM}+/{^p>5_eI~]g8I+j?tJ}. ciGVP!}x}IK,MyT(LqTfMY(wOqN8)'
