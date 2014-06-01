# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Serie'
        db.create_table(u'manga_serie', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('capitulos', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'manga', ['Serie'])

        # Adding model 'Capitulo'
        db.create_table(u'manga_capitulo', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manga.Serie'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=90)),
        ))
        db.send_create_signal(u'manga', ['Capitulo'])

        # Adding model 'Pagina'
        db.create_table(u'manga_pagina', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('capitulo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manga.Capitulo'])),
        ))
        db.send_create_signal(u'manga', ['Pagina'])


    def backwards(self, orm):
        # Deleting model 'Serie'
        db.delete_table(u'manga_serie')

        # Deleting model 'Capitulo'
        db.delete_table(u'manga_capitulo')

        # Deleting model 'Pagina'
        db.delete_table(u'manga_pagina')


    models = {
        u'manga.capitulo': {
            'Meta': {'ordering': "('num', 'titulo')", 'object_name': 'Capitulo'},
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manga.Serie']"}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        u'manga.pagina': {
            'Meta': {'ordering': "('num',)", 'object_name': 'Pagina'},
            'capitulo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['manga.Capitulo']"}),
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {})
        },
        u'manga.serie': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Serie'},
            'capitulos': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        }
    }

    complete_apps = ['manga']