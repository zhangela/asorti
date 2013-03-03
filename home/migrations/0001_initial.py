# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BetaSignup'
        db.create_table('home_betasignup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('signed_up_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('home', ['BetaSignup'])


    def backwards(self, orm):
        
        # Deleting model 'BetaSignup'
        db.delete_table('home_betasignup')


    models = {
        'home.betasignup': {
            'Meta': {'object_name': 'BetaSignup'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'signed_up_on': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['home']
