# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',

    url(r'^$', TemplateView.as_view(template_name='index.html')),  # sorry!
    url(r'^catalogo/', include('apps.catalogo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
