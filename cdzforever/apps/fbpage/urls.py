# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import TokenRequestView, StoreTokenView, AgendarFormView

urlpatterns = patterns(
    '',

    url(r'^token/$', TokenRequestView.as_view(), name='token'),
    url(r'^store_token/$', StoreTokenView.as_view(), name='store_token'),
    url(r'^agendar/$', AgendarFormView.as_view(), name='agendar'),
)
