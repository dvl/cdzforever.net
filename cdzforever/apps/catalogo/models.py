# -*- coding: utf-8 -*-

from django_pg import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from . import choices


class Serie(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    nome = models.CharField(max_length=90)
    audio = models.CharField(choices=choices.AUDIO, max_length=5)
    legenda = models.CharField(choices=choices.LEGENDA, max_length=5, blank=True, null=True)

    episodios = models.IntegerField('Total de Episódios', blank=True, null=True)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)

    @property
    def episodios_disponiveis(self):
        return self.episodio_set.count()    


class Episodio(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    serie = models.ForeignKey(Serie)

    num = models.IntegerField()
    titulo = models.CharField(max_length=90)
    sinopse = models.TextField(blank=True, null=True)

    screenshot = models.ImageField(upload_to='screenshots', blank=True, null=True)
    screenshot_thumbnail = ImageSpecField(source='screenshot',
                                      processors=[ResizeToFill(125, 70)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __unicode__(self):
        return '%d - %s' % (self.num, self.titulo)

    class Meta:
        ordering = ('num', 'titulo')


class Servidor(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    nome = models.CharField(max_length=90)
    url = models.URLField()

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)


class Link(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    tipo = models.CharField(choices=choices.TIPO_LINK, max_length=10)
    servidor = models.ForeignKey(Servidor)
    episodio = models.ForeignKey(Episodio)

    url = models.URLField()

    def __unicode__(self):
        return self.url
