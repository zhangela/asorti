from django.http import HttpResponse
from django.shortcuts import render
from data.models import *
from data.GenericScraper import *
from data.AbercrombieScraper import *
from data.TopshopScraper import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_item(request, item_id):
    context = {'item' : Item.objects.get(id=item_id), 'type_reverse' : type_reverse}
    return render(request, 'data/item.html', context)

def scrape(request, store):
    scraper = eval(store + 'ScraperClass')()
    scraper.scrape()   

def catalog(request):
    #store = request.GET.get('store', None)
    store = "Abercrombie"
    category = request.GET.get('category', None)
    print store, category
    if store and category:
        items = Item.objects.filter(store=store, type=type[category])
    elif store:
        items = Item.objects.filter(store=store)
    elif category:
        items = Item.objects.filter(type=type[category])
    else:
        items = Item.objects.all()
    
    paginator = Paginator(items, 50)
    
    page = request.GET.get('page')
    try:
	item_subset = paginator.page(page)
    except PageNotAnInteger:
	item_subset = paginator.page(1)
    except EmptyPage:
	item_subset = paginator.page(paginator.num_pages)

    return render(request, 'data/catalog.html', {'items' : item_subset})

def catalog_by_store(request, store):
    return
 
