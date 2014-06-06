# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

from django_markdown import flatpages

from apps.blog.views import PostListView

admin.autodiscover()
flatpages.register()

urlpatterns = patterns(
    '',

    url(r'^$', PostListView.as_view(), name='index'),

    url(r'^catalogo/', include('apps.catalogo.urls', namespace='catalogo')),
    url(r'^manga/', include('apps.manga.urls', namespace='manga')),
    url(r'^fb/', include('apps.fbpage.urls', namespace='fb')),

    url(r'^pages/', include('django.contrib.flatpages.urls')),

    url(r'^markdown/', include('django_markdown.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
