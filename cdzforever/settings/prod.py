# -*- coding: utf-8 -*-

from base import *

import dj_database_url

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['*']
