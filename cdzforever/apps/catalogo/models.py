# -*- coding: utf-8 -*-

from django_pg import models

from . import choices


class Serie(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    nome = models.CharField(max_length=90)
    audio = models.CharField(choices=choices.AUDIO, max_length=5)
    legenda = models.CharField(choices=choices.LEGENDA, max_length=5, blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Episodio(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    serie = models.ForeignKey(Serie)

    num = models.IntegerField()
    titulo = models.CharField(max_length=90)
    sinopse = models.TextField(blank=True, null=True)

    link = models.URLField()
    legenda = models.URLField(blank=True, null=True)
    screenshot = models.URLField(blank=True, null=True)

    def __unicode__(self):
        return '%d - %s' % (self.num, self.titulo)

    class Meta:
        ordering = ('num', 'titulo')
