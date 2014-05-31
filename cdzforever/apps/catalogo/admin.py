# -*- coding: utf-8 -*-

from django.contrib import admin

from models import Servidor, Link, Serie, Episodio


class SerieAdmin(admin.ModelAdmin):
    list_display = ('nome', 'episodios_disponiveis', 'episodios', 'audio',
                    'legenda')
    list_filter = ('audio', 'legenda')
    search_fields = ('nome',)


class LinkInline(admin.TabularInline):
    model = Link
    extra = 3


class EpisodioAdmin(admin.ModelAdmin):
    list_display = ('num', 'titulo', 'serie', 'acessos')
    list_display_links = ('titulo', 'serie')
    list_filter = ('serie',)
    search_fields = ('titulo',)

    inlines = [LinkInline]

admin.site.register(Serie, SerieAdmin)
admin.site.register(Episodio, EpisodioAdmin)
admin.site.register(Servidor)
