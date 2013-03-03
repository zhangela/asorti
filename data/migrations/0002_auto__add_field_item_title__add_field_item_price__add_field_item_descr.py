# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Item.title'
        db.add_column('data_item', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=1000), keep_default=False)

        # Adding field 'Item.price'
        db.add_column('data_item', 'price', self.gf('django.db.models.fields.FloatField')(default=-1), keep_default=False)

        # Adding field 'Item.description'
        db.add_column('data_item', 'description', self.gf('django.db.models.fields.CharField')(default='', max_length=5000), keep_default=False)

        # Adding field 'Item.keywords'
        db.add_column('data_item', 'keywords', self.gf('django.db.models.fields.CharField')(default='', max_length=1000), keep_default=False)

        # Adding field 'Item.color'
        db.add_column('data_item', 'color', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Item.title'
        db.delete_column('data_item', 'title')

        # Deleting field 'Item.price'
        db.delete_column('data_item', 'price')

        # Deleting field 'Item.description'
        db.delete_column('data_item', 'description')

        # Deleting field 'Item.keywords'
        db.delete_column('data_item', 'keywords')

        # Deleting field 'Item.color'
        db.delete_column('data_item', 'color')


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
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['data']
