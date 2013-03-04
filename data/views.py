from django.http import HttpResponse
from django.shortcuts import render
from data.models import *
from data.GenericScraper import *
from data.AbercrombieScraper import *

def get_item(request, item_id):
    context = {'item' : Item.objects.get(id=item_id)}
    return render(request, 'data/item.html', context)

def scrape(request, store):
    print "got scrape request"
    scraper = eval(store + 'ScraperClass')()
    scraper.scrape()   

def catalog(request):
    return

def catalog_by_store(request, store):
    return
 
