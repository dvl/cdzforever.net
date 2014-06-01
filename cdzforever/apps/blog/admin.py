# -*- coding: utf-8 -*-

from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from .models import Post


admin.site.register(Post, MarkdownModelAdmin)
