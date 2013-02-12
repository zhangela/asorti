from django.db import models
from data.models import *

occasion_reverse = {1 : 'Black-tie event', 2 : 'Casual outing', 3 : 'Date', 4 : 'Party', 5 : 'Work'}
occasion = {'Black-tie event' : 1, 'Casual outing' : 2, 'Date' : 3, 'Party' : 4, 'Work' : 5}

style_reverse = {1 : 'Casual', 2 : 'Classic', 3 : 'Conservative', 4 : 'Dramatic', 5 : 'Edgy', 6 : 'Elegant', 7 : 'Feminine', 8 : 'Grunge', 9 : 'Sexy', 10 : 'Vintage'}
style = {'Casual' : 1, 'Classic' : 2, 'Conservative' : 3, 'Dramatic' : 4, 'Edgy' : 5, 'Elegant' : 6, 'Feminine' : 7, 'Grunge' : 8, 'Sexy' : 9, 'Vintage' : 10}

quality = {'Great' : 1, 'Bad' : 2}
quality_reverse = {1 : 'Great', 2 : 'Bad'}

class Outfit(models.Model):
    rating = models.IntegerField()
    rainy = models.BooleanField()
    weather = models.IntegerField()
    occasion = models.IntegerField()
    style = models.IntegerField()
    description = models.CharField(max_length=1000, blank=True, null=True)

class OutfitItem(models.Model):
    outfit = models.ForeignKey(Outfit)
    item = models.ForeignKey(Item)

class PairRating(models.Model):
    item1 = models.ForeignKey(Item, related_name = 'item1')
    item2 = models.ForeignKey(Item, related_name = 'item2')
    rating = models.IntegerField()
    outfit = models.ForeignKey(Outfit)
