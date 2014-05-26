# -*- coding: utf-8 -*-

from django.contrib import admin

from models import Serie, Episodio


class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome', 'audio', 'legenda')
    list_filter = ('audio', 'legenda')
    search_fields = ('nome',)


class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('num', 'titulo', 'serie')
    list_display_links = ('titulo', 'serie')
    list_filter = ('serie',)
    search_fields = ('titulo',)

admin.site.register(Serie, SerieAdmin)
admin.site.register(Episodio, EpisodioAdmin)
