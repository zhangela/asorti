from django.shortcuts import render, redirect
from django.http import HttpResponse
from ratings.models import *
from data.models import *
from ratings.models import *
from django.core.context_processors import csrf
import random
import json
from django.utils import simplejson
from django.core import serializers
from data.CustomEncoder import *

UNKNOWN = 0
OUTFIT_WITH_ITEM = 1
OUTFIT_WITH_ITEM_TYPE = 2
OUTFIT_WITHOUT_ITEM_TYPE = 3
num_rec = 3


def get_associated_items(request, item_id):
    # get rec
    input = {"class" : "item", "item_id" : item_id}

    item = Item.objects.get(id=item_id)
    type = item.type
    store = item.store

    list_of_associated_items = []

    if item.associatedItems:
        list_of_associated_items = item.associatedItems
    else:
        items_of_the_same_type = list(Item.objects.filter(type=type))
        list_of_associated_items = random.sample(items_of_the_same_type, num_rec)

    context = {'outfits' : list_of_associated_items, 'item' : Item.objects.get(id=item_id), 'high_level_category_reverse' : high_level_category_reverse, 'style_reverse' : style_reverse, 'occasion_reverse' : occasion_reverse, 'type_reverse' : type_reverse}
    return render(request, 'recommender/associated_items.html', context)

def get_recommendation(request, item_id):
    # get rec
    input = {"class" : "item", "item_id" : item_id}
    curr_rec = []
    outfits_used = []
    for i in range(num_rec):
        rec = get_recommendation_helper(request, input, outfits_used)
        if rec == None:
            break
        curr_rec = curr_rec + [rec]
	print rec[0].id
        outfits_used = outfits_used + [rec[0]]
    context = {'outfits' : curr_rec, 'item' : Item.objects.get(id=item_id), 'high_level_category_reverse' : high_level_category_reverse, 'style_reverse' : style_reverse, 'occasion_reverse' : occasion_reverse, 'type_reverse' : type_reverse}
    return render(request, 'recommender/recommendations.html', context)

def get_recommendation_helper(request, input, outfits_used):
    store = None
    state = UNKNOWN
    outfit = None
    item_id = input.get("item_id")
    type = input.get("item_type")
    if type:
	type = int(type)
    if (input["class"] == "item"):
        # if item_id in an outfit, return that outfit
        item = Item.objects.get(id=item_id)
        type = item.type
        store = item.store

        #outfit with item exists
        outfit_items = OutfitItem.objects.exclude(outfit__in = outfits_used).filter(item=item, outfit__rating=quality['Great'])
        if (len(outfit_items) > 0):
            outfit = outfit_items[0].outfit
            state = OUTFIT_WITH_ITEM
    if (outfit == None):
        # outfit with item doesn't exist
        # if not, get item type, pick random outfit containing that type, substitute and return
        # todo: next step - get most similar top that is in an outfit
	if store:
            items_with_correct_type = Item.objects.filter(type=type, store=store)
        else:
            items_with_correct_type = Item.objects.filter(type=type)

        outfit_items = OutfitItem.objects.filter(item__in = items_with_correct_type, outfit__rating=quality['Great']).exclude(outfit__in = outfits_used)
        if (len(outfit_items) > 0):
            # get the corresponding outfit
            outfit = outfit_items[random.randint(0, len(outfit_items)-1)].outfit
            print outfit.id
            state = OUTFIT_WITH_ITEM_TYPE
        else:
            # get a random outfit and add
            used_ids = []
            for outfit in outfits_used:
                used_ids = used_ids + [outfit.id]
	    if store:
            	outfits_temp = OutfitItem.objects.exclude(outfit__id__in = used_ids).filter(outfit__rating=quality['Great'], item__store=store).order_by('?')
	    else:
		outfits_temp = OutfitItem.objects.exclude(outfit__id__in = used_ids).filter(outfit__rating=quality['Great']).order_by('?')
            if (len(outfits_temp) > 0):
            	outfit = outfits_temp[0].outfit
	    else:
               return None
            state = OUTFIT_WITHOUT_ITEM_TYPE

    outfit_items = OutfitItem.objects.filter(outfit=outfit)
    items = []
    substituted = False
    for outfit_item in outfit_items:
        if (state == OUTFIT_WITH_ITEM_TYPE):
            if ((outfit_item.item.type == type) and (substituted == False)):
                substituted = True
                continue
        items = items + [outfit_item.item]
    if (not (state == OUTFIT_WITH_ITEM) and (input["class"]=="item")):
        items = make_valid_outfit(items, item)
        items = items + [item]
    top = None
    for item in items:
        if (item.type == 'tops') or (item.type == 'dresses'):
            items.remove(item)
            top = item
    if top:
        items = top + items
    return [outfit, items]

def make_valid_outfit(items, extra_item):
    # extra_item's type will determine what to check:
    item_type = type_reverse[extra_item.type]
    to_remove = { 'dresses' : ['tops', 'jeans', 'shorts', 'skirts', 'leggings-pants'],
		 'tops' : ['dresses'],
		 'jeans' : ['dresses', 'shorts', 'skirts', 'leggings-pants'],
		 'skirts' : ['jeans', 'shorts', 'dresses', 'leggings-pants'],
		 'shorts' : ['jeans', 'dresses', 'skirts', 'leggings-pants'],
		 'leggings-pants' : ['jeans', 'dresses', 'skirts', 'dresses']}

    for item in items:
	if (item_type in to_remove) and (type_reverse[item.type] in to_remove[item_type]):
	    items.remove(item)
    return items

def get_recommendation_by_type(request, item_type):
    input = {"class" : "type", "item_type" : item_type}
    curr_rec = []
    outfits_used = []
    for i in range(num_rec):
        rec = get_recommendation_helper(request, input, outfits_used)
        if rec == None:
            break
        curr_rec = curr_rec + [rec]
        outfits_used = outfits_used + [rec[0]]
    recs = []
    return HttpResponse(json.dumps(curr_rec, cls=CustomTypeEncoder), mimetype='application/json')
