# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Reporte'
        db.create_table(u'catalogo_reporte', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Link'])),
            ('motivo', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('descricao', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['Reporte'])


    def backwards(self, orm):
        # Deleting model 'Reporte'
        db.delete_table(u'catalogo_reporte')


    models = {
        u'catalogo.episodio': {
            'Meta': {'ordering': "('num', 'titulo')", 'object_name': 'Episodio'},
            'acessos': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
        u'catalogo.reporte': {
            'Meta': {'object_name': 'Reporte'},
            'descricao': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['catalogo.Link']"}),
            'motivo': ('django.db.models.fields.CharField', [], {'max_length': '90'})
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