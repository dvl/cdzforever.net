# -*- coding: utf-8 -*-

from django.conf import settings


def inject_fb_app_id(request):
    return {
        'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID
    }
