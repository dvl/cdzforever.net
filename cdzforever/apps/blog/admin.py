# -*- coding: utf-8 -*-

from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from .models import Post


class PostAdmin(MarkdownModelAdmin, admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    list_filter = ('autor',)
    search_fields = ('titulo', 'corpo')
    fields = ('titulo', 'corpo')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'autor', None) is None:
            obj.autor = request.user

        obj.save()

admin.site.register(Post, PostAdmin)
