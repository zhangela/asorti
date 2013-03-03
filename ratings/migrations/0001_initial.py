# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Outfit'
        db.create_table('ratings_outfit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('rainy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('weather', self.gf('django.db.models.fields.IntegerField')()),
            ('occasion', self.gf('django.db.models.fields.IntegerField')()),
            ('style', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal('ratings', ['Outfit'])

        # Adding model 'OutfitItem'
        db.create_table('ratings_outfititem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('outfit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Outfit'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Item'])),
        ))
        db.send_create_signal('ratings', ['OutfitItem'])

        # Adding model 'PairRating'
        db.create_table('ratings_pairrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item1', to=orm['data.Item'])),
            ('item2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='item2', to=orm['data.Item'])),
            ('rating', self.gf('django.db.models.fields.IntegerField')()),
            ('outfit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ratings.Outfit'])),
        ))
        db.send_create_signal('ratings', ['PairRating'])


    def backwards(self, orm):
        
        # Deleting model 'Outfit'
        db.delete_table('ratings_outfit')

        # Deleting model 'OutfitItem'
        db.delete_table('ratings_outfititem')

        # Deleting model 'PairRating'
        db.delete_table('ratings_pairrating')


    models = {
        'data.item': {
            'Meta': {'object_name': 'Item'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'high_level_category': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        'ratings.outfit': {
            'Meta': {'object_name': 'Outfit'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occasion': ('django.db.models.fields.IntegerField', [], {}),
            'rainy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rating': ('django.db.models.fields.IntegerField', [], {}),
            'style': ('django.db.models.fields.IntegerField', [], {}),
            'weather': ('django.db.models.fields.IntegerField', [], {})
        },
        'ratings.outfititem': {
            'Meta': {'object_name': 'OutfitItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Item']"}),
            'outfit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Outfit']"})
        },
        'ratings.pairrating': {
            'Meta': {'object_name': 'PairRating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item1'", 'to': "orm['data.Item']"}),
            'item2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'item2'", 'to': "orm['data.Item']"}),
            'outfit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Outfit']"}),
            'rating': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['ratings']
