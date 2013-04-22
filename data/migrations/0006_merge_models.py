# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

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
        },
        u'data.scrapedrecommendations': {
            'Meta': {'object_name': 'ScrapedRecommendations'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item'", 'to': u"orm['data.Item']"}),
            'rec_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rec_item'", 'to': u"orm['data.Item']"})
        }
    }

    complete_apps = ['data']