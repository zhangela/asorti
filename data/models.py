from django.db import models

high_level_category = {'clothing' : 1, 'accessories' : 2, 'shoes' : 3}
type = {'shoes' : 1, 'accessories' : 2, 'bags-and-purses' : 3, 'jewelry' : 4, 'tops' : 5, 'dresses' : 6, 'jeans' : 7, 'leggings-pants' : 8, 'skirts' : 9, 'shorts' : 10, 'outerwear' : 11}

high_level_category_reverse = {1 : 'clothing', 2 : 'accessories', 3 : 'shoes'}
type_reverse = {1 : 'shoes', 2 : 'accessories', 3 : 'bags-and-purses', 4 : 'jewelry', 5 : 'tops', 6 : 'dresses', 7 : 'jeans', 8 : 'leggings-pants', 9 : 'skirts', 10 : 'shorts', 11 : 'outerwear'}

class Item(models.Model):
    filename = models.CharField(max_length=200)
    high_level_category = models.IntegerField()
    type = models.IntegerField()
    # need to store the extra info
    title = models.CharField(max_length=1000, default="")
    price = models.FloatField(default=-1)
    description = models.CharField(max_length=5000, default="")
    keywords = models.CharField(max_length=1000, default="")
    color = models.CharField(max_length=100, default="")
