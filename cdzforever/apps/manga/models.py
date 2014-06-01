# -*- coding: utf-8 -*-

import os

from django_pg import models


class Serie(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    nome = models.CharField(max_length=90)

    capitulos = models.IntegerField('Total de Capítulos', blank=True, null=True)

    def __unicode__(self):
        return self.nome

    @property
    def capitulos_disponiveis(self):
        return self.capitulo_set.count()

    class Meta:
        ordering = ('nome',)


class Capitulo(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    serie = models.ForeignKey(Serie)

    num = models.IntegerField()
    titulo = models.CharField(max_length=90)

    class Meta:
        ordering = ('num', 'titulo')

    def __unicode__(self):
        return '#%s - %s' % (self.num, self.titulo)


def pagina_filename(instace, filename):
    file, ext = os.path.splitext(filename)

    serie = instace.serie.pk
    capitulo = instace.capitulo.pk
    pagina = instace.pk

    return os.path.join(serie, capitulo, '%s%s' % (pagina, ext))


class Pagina(models.Model):
    id = models.UUIDField(auto_add=True, primary_key=True)

    num = models.IntegerField()

    capitulo = models.ForeignKey(Capitulo)

    image = models.ImageField(upload_to=pagina_filename)

    class Meta:
        ordering = ('num',)

    def __unicode__(self):
        return 'Página %s' % self.num
