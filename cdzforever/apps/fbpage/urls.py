# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from .views import AgendarFormView

urlpatterns = patterns(
    '',

    url(r'^agendar/$', AgendarFormView.as_view(), name='agendar'),
)
