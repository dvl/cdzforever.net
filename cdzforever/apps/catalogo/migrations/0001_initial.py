# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Serie'
        db.create_table(u'catalogo_serie', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('audio', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('legenda', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('episodios', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['Serie'])

        # Adding model 'Episodio'
        db.create_table(u'catalogo_episodio', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('serie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Serie'])),
            ('num', self.gf('django.db.models.fields.IntegerField')()),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('sinopse', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('screenshot', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'catalogo', ['Episodio'])

        # Adding model 'Servidor'
        db.create_table(u'catalogo_servidor', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=90)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'catalogo', ['Servidor'])

        # Adding model 'Link'
        db.create_table(u'catalogo_link', (
            ('id', self.gf('django_pg.models.fields.uuid.UUIDField')(auto_add=u'uuid:uuid4', primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('servidor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Servidor'])),
            ('episodio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['catalogo.Episodio'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'catalogo', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Serie'
        db.delete_table(u'catalogo_serie')

        # Deleting model 'Episodio'
        db.delete_table(u'catalogo_episodio')

        # Deleting model 'Servidor'
        db.delete_table(u'catalogo_servidor')

        # Deleting model 'Link'
        db.delete_table(u'catalogo_link')


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