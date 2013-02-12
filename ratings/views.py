from django.http import HttpResponse
from django.shortcuts import render, redirect
from ratings.models import *
from data.models import *
from django.core.context_processors import csrf

#@csrf_exempt
def create_and_rate_outfit(request):
    if request.method == 'POST':
        #get outfit ratings
        rating = int(request.POST['outfit_quality'])
        weather = int(request.POST['outfit_weather'])
        if 'outfit_rainy' in request.POST.keys():
            rainy = True
        else:
            rainy = False
	occasion = int(request.POST['outfit_occasion'])
        style = int(request.POST['outfit_style'])

	if (('description' in request.POST.keys()) and (request.POST['description'].strip() != 'Optional')):
	    description = request.POST['description'].strip()
	    outfit = Outfit(rating=rating, weather=weather, rainy=rainy, occasion=occasion, style=style, description=description)
	else:
	    outfit = Outfit(rating=rating, weather=weather, rainy=rainy, occasion=occasion, style=style)
        outfit.save()

        #get items in outfit
        items = request.POST['items'].split('__and__')[1:]
        for item in items:
            item_id = int(item.split('-')[1])
            new_item = OutfitItem(outfit=outfit, item=Item.objects.get(id=item_id))
            new_item.save()

        #get pairs and ratings
        post_sub = slicedict(request.POST, 'pair_rating_')
        for key, value in post_sub.items():
            items = key.split('__and__')
            item1_id = int(items[0].split('-')[1])
            item2_id = int(items[1].split('-')[1])
            rating = int(value)
            pair_rating = PairRating(item1=Item.objects.get(id=item1_id), item2=Item.objects.get(id=item2_id), rating=rating, outfit=outfit)
            pair_rating.save()
        return redirect('createandrate')
    else:
        #if form doesn't validate, show the creation page
        tops = Item.objects.filter(type = type['tops'])
        dresses = Item.objects.filter(type = type['dresses'])
        shoes = Item.objects.filter(type = type['shoes'])
        accessories = Item.objects.filter(type = type['accessories'])
        jeans = Item.objects.filter(type = type['jeans'])
        leggings_pants = Item.objects.filter(type = type['leggings-pants'])
        bags_and_purses = Item.objects.filter(type = type['bags-and-purses'])
        jewelry = Item.objects.filter(type = type['jewelry'])
        skirts = Item.objects.filter(type = type['skirts'])
        shorts = Item.objects.filter(type = type['shorts'])
        outerwear = Item.objects.filter(type = type['outerwear'])
        types = [tops, dresses, shoes, accessories, jeans, leggings_pants, bags_and_purses, jewelry, skirts, shorts, outerwear]

    context = {'types' : {'Tops' : tops, 'Dresses' : dresses, 'Shoes' : shoes, 'Accessories' : accessories, 'Jeans' : jeans, 'Leggings_and_Pants' : leggings_pants, 'Bags_and_Purses' : bags_and_purses, 'Jewelry' : jewelry, 'Skirts' : skirts, 'Shorts' : shorts, 'Outerwear' : outerwear} }
    context.update(csrf(request))
    return render(request, 'ratings/createandrate.html', context)


def slicedict(d, s):
    return {k:v for k,v in d.iteritems() if k.startswith(s)}

def getoutfit(request, outfit_id):
    outfit = Outfit.objects.get(id=outfit_id)
    outfit_items = OutfitItem.objects.filter(outfit=outfit)
    items = []
    for outfit_item in outfit_items:
        items = items + [outfit_item.item]
    context = {'outfit' : [outfit, items], 'high_level_category_reverse' : high_level_category_reverse, 'occasion_reverse' : occasion_reverse, 'style_reverse' : style_reverse}
    return render(request, 'ratings/showoutfit.html', context)

def ratepair(request, outfit_id):
    if request.method == 'POST':
        outfit = Outfit.objects.get(id=outfit_id)
        post_sub = slicedict(request.POST, 'pair_rating_')
        for key, value in post_sub.items():
            key = key.split('pair_rating_')[1]
            items = key.split('__and__')
            item1_id = int(items[0])
            item2_id = int(items[1])
            rating = int(value)
            print item1_id, item2_id, rating
            pair_rating = PairRating(item1=Item.objects.get(id=item1_id), item2=Item.objects.get(id=item2_id), rating=rating, outfit=outfit)
            pair_rating.save()
        return redirect('ratepair', outfit_id=(int(outfit_id)+1))
    else:
        outfit_items = OutfitItem.objects.filter(outfit=Outfit.objects.get(id=outfit_id))
        pairs = []
        for i in range(0,len(outfit_items)):
            for j in range((i+1),len(outfit_items)):
                pairs = pairs + [[outfit_items[i].item, outfit_items[j].item]]
        context = {'pairs' : pairs}
        print pairs
        context.update(csrf(request))
        return render(request, 'ratings/ratepair.html', context)
