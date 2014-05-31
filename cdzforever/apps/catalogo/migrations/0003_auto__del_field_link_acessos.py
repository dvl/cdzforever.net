# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Link.acessos'
        db.delete_column(u'catalogo_link', 'acessos')


    def backwards(self, orm):
        # Adding field 'Link.acessos'
        db.add_column(u'catalogo_link', 'acessos',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    models = {
        u'catalogo.episodio': {
            'Meta': {'ordering': "('num', 'titulo')", 'object_name': 'Episodio'},
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Serie']"}),
            'sinopse': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        u'catalogo.link': {
            'Meta': {'object_name': 'Link'},
            'episodio': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Episodio']"}),
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'servidor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Servidor']"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'catalogo.serie': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Serie'},
            'audio': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'episodios': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'legenda': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '90'})
        },
        u'catalogo.servidor': {
            'Meta': {'ordering': "('nome',)", 'object_name': 'Servidor'},
            'id': ('django_pg.models.fields.uuid.UUIDField', [], {u'auto_add': "u'uuid:uuid4'", 'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['catalogo']