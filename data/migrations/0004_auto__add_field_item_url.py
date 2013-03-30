# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Item.url'
        db.add_column('data_item', 'url', self.gf('django.db.models.fields.CharField')(default='', max_length=1000), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Item.url'
        db.delete_column('data_item', 'url')


    models = {
        'data.item': {
            'Meta': {'object_name': 'Item'},
            'color': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5000'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'high_level_category': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '-1'}),
            'store': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'})
        }
    }

    complete_apps = ['data']
