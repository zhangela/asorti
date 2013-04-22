# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'data_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('high_level_category', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
            ('price', self.gf('django.db.models.fields.FloatField')(default=-1)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=5000)),
            ('keywords', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
            ('color', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('store', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('url', self.gf('django.db.models.fields.CharField')(default='', max_length=1000)),
        ))
        db.send_create_signal(u'data', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'data_item')


    models = {
        u'data.item': {
            'Meta': {'object_name': 'Item'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5000'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'high_level_category': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'store': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'})
        }
    }

    complete_apps = ['data']