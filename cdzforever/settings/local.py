# -*- coding: utf-8 -*-

from base import *

SECRET_KEY = '+o-k_3(=c76o+u-f3ltllvq=0q6cib8&q+)ooh7*hw#@keq8y$'

DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "cdzforever",
        "USER": "postgres",
        "PASSWORD": "deadpool",
        "HOST": "localhost",
        "PORT": "5432",
    },
}
