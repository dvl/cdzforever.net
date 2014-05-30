# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/dvl/Projects/cdzforever.net/data')  # fuck

import os

from django.core.files import File
from django.core.management.base import BaseCommand

from apps.catalogo.models import Serie, Servidor, Episodio, Link

series = {
    'cdz': 'Os Cavaleiros do Zodiaco',
    'hades': 'The Hades Chapter',
    'lc_dub': 'The Lost Canvas',
    'lc_leg': 'The Lost Canvas',
    'filmes': 'Filmes',
}

mega = Servidor.objects.get(nome='Mega')
shared = Servidor.objects.get(nome='4Shared')
minhateca = Servidor.objects.get(nome='Minhateca')


def get_servidor_by_url(url):
    if 'mega' in url:
        return mega
    elif '4shared' in url:
        return shared
    elif 'minhateca' in url:
        return minhateca
    else:
        raise Exception('Shit')


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        import gerador

        for key, serie in series.iteritems():
            dados = getattr(gerador, key)

            s = Serie(nome=serie, audio='JP', legenda='PT-BR')
            s.save()

            for ep in dados:
                e = Episodio(serie=s, num=ep['num'], titulo=ep['titulo'])
                # e.screenshot.save(os.path.basename(ep['screenshot']), File(open(ep['screenshot'])))
                e.save()

                for episodio in ep['links']:
                    l = Link(tipo='episodio', servidor=get_servidor_by_url(episodio), episodio=e, url=episodio)
                    l.save()

                for legenda in ep['legendas']:
                    if legenda:
                        l = Link(tipo='legenda', servidor=get_servidor_by_url(legenda), episodio=e, url=legenda)
                        l.save()
