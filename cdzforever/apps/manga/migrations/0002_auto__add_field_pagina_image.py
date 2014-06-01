# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pagina.image'
        db.add_column(u'manga_pagina', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pagina.image'
        db.delete_column(u'manga_pagina', 'image')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
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