from bs4 import BeautifulSoup
from soupselect import select
import urlparse
import html5lib
import html5lib.treebuilders
import urllib
import urllib2
import os
import errno
import re
import uuid
from django.conf import settings
from data.models import *
from GenericScraper import *

<<<<<<< HEAD
class GenericScraper:

    urls = {}
=======
class AbercrombieScraperClass(GenericScraperClass):

    type_mapping = {'tops' : 'tops', 'tees' : 'tops', 'shirts' : 'tops', 'polos' : 'tops', 'hoodies' : 'outerwear', 'shorts' : 'shorts', 'jeans' : 'jeans', 'sweatpants' : 'jeans', 'pants' : 'leggings-pants', 'yoga' : 'jeans', 'skirts' : 'skirts', 'dresses' : 'dresses', 'flipflops' : 'shoes', 'accessories' : 'accessories', 'outerwear' : 'outerwear', 'sweaters' : 'tops'}

    urls = {
    "tops": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=120207&catalogId=10901&langId=-1&categoryId=120207&storeId=10051&topCategoryId=12203",
    "tees": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=120206&catalogId=10901&langId=-1&categoryId=120206&storeId=10051&topCategoryId=12203",
    "shirts": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=120205&catalogId=10901&langId=-1&categoryId=120205&storeId=10051&topCategoryId=12203",
    "polos": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=119705&catalogId=10901&langId=-1&categoryId=119705&storeId=10051&topCategoryId=12203",
    "hoodies": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12843&catalogId=10901&langId=-1&categoryId=12843&storeId=10051&topCategoryId=12203",
    "sweaters": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12282&catalogId=10901&langId=-1&categoryId=12282&storeId=10051&topCategoryId=12203",
    "outerwear": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12252&catalogId=10901&langId=-1&categoryId=12252&storeId=10051&topCategoryId=12203",
    "shorts": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12262&catalogId=10901&langId=-1&categoryId=12262&storeId=10051&topCategoryId=12203",
    "jeans": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12261&catalogId=10901&langId=-1&categoryId=12261&storeId=10051&topCategoryId=12203",
    "sweatpants": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12272&catalogId=10901&langId=-1&categoryId=12272&storeId=10051&topCategoryId=12203",
    "pants": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12267&catalogId=10901&langId=-1&categoryId=12267&storeId=10051&topCategoryId=12203",
    "yoga": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=73463&catalogId=10901&langId=-1&categoryId=73463&storeId=10051&topCategoryId=12203",
    "skirts": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=13058&catalogId=10901&langId=-1&categoryId=13058&storeId=10051&topCategoryId=12203",
    "dresses": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12265&catalogId=10901&langId=-1&categoryId=12265&storeId=10051&topCategoryId=12203",
    "flipflops": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=13056&catalogId=10901&langId=-1&categoryId=13056&storeId=10051&topCategoryId=12203",
    "accessories":"http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=13060&catalogId=10901&langId=-1&categoryId=13060&storeId=10051&topCategoryId=12203"
    }
>>>>>>> e2fa226f3ff807dd1bfcfdba0c4d8c9decbd1c9b
    
    def __init__(self, urls):
        self.urls = urls

<<<<<<< HEAD
    def scrape(self):
        for category in self.urls.keys():
            self.scrapeCategory(category)

    def scrapeCategory(self, category):
        # read page using beautiful soup
        fd = urllib2.urlopen(self.urls[category])
        parsed = BeautifulSoup(fd)

        # isolate items
        items = self.findItems(parsed)

        # process Items
        for item in items:
            fd = urllib2.urlopen(item)
            parsed = BeautifulSoup(fd)
            self.processItem(parsed, item, category)

    # subclasses must define
    # takes in page parsed by beautiful soup and produces 
    # a list of item (url + possibly some metadata), i.e.
    # produces a list of tuples. Assume that the first entry
    # in list is the url
    def findItems(self, parsed):
        # items = []
        # find item urls and metadata
        # return items
        raise "Method not implemented"

    def processItem(self, parsed, item):
        # get image, save
        # get title
        # get price
        # get color
        # get metadata
        # create item in database and save #cannot do right now -AZ
        raise "Method not implemented"


class AbercrombieScraper(GenericScraper):

    store = ""
    
    def __init__(self, urls, store):
        GenericScraper.__init__(self, urls)
        self.store = "Abercrombie"

=======
>>>>>>> e2fa226f3ff807dd1bfcfdba0c4d8c9decbd1c9b
    # takes in page parsed by beautiful soup and produces 
    # a list of item (url + possibly some metadata), i.e.
    # produces a list of tuples. Assume that the first entry
    # in list is the url
    def findItems(self, parsed):
        items = []
        links = parsed.find_all('h3')
        for link in links:
            if 'data-productid' in str(link):
                items.append("http://www.abercrombie.com" + str(link.find('a')['href']))
        return items

    def processItem(self, parsed, item, itemCategory):
        d = {}
        d ['store'] = self.store
        d['type'] = type[self.type_mapping[itemCategory]]
        d['high_level_category'] = high_level_category[type_to_high_level_category[self.type_mapping[itemCategory]]]
        d['description'] = ""
        d['keywords'] = ""
        d['title'] = ""
        image = ""

        d['price'] = parsed.find('div', class_='price').find(class_='offer-price').getText().replace("$", "")
        d['color'] = parsed.find('span', class_='color').getText()
        meta = parsed.find_all('meta')

        for data in meta:
            strData = str(data)
            if 'property="og:description"' in strData:
                d['description'] = data['content']
            elif 'name="keywords"' in strData:
                d['keywords'] = data['content'] + ',' + itemCategory
            elif 'property="og:title"' in strData:
                d['title'] = data['content']
            elif 'property="og:image"' in strData:
                image = data['content']

<<<<<<< HEAD
        print "TITLE: " + title + ", CATEGORY: " + category + ", PRICE: " + price + ", COLOR: " + color + ", IMAGE: " + image
        # create item in database and save #cannot do right now -AZ



urls = {
"tops": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=120207&catalogId=10901&langId=-1&categoryId=120207&storeId=10051&topCategoryId=12203",
"tees": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=120206&catalogId=10901&langId=-1&categoryId=120206&storeId=10051&topCategoryId=12203",
"shirts": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=120205&catalogId=10901&langId=-1&categoryId=120205&storeId=10051&topCategoryId=12203",
"polos": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=119705&catalogId=10901&langId=-1&categoryId=119705&storeId=10051&topCategoryId=12203",
"hoodies": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12843&catalogId=10901&langId=-1&categoryId=12843&storeId=10051&topCategoryId=12203",
"sweathers": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12282&catalogId=10901&langId=-1&categoryId=12282&storeId=10051&topCategoryId=12203",
"outerwear": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12252&catalogId=10901&langId=-1&categoryId=12252&storeId=10051&topCategoryId=12203",
"shorts": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12262&catalogId=10901&langId=-1&categoryId=12262&storeId=10051&topCategoryId=12203",
"jeans": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12261&catalogId=10901&langId=-1&categoryId=12261&storeId=10051&topCategoryId=12203",
"sweatpants": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12272&catalogId=10901&langId=-1&categoryId=12272&storeId=10051&topCategoryId=12203",
"pants": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12267&catalogId=10901&langId=-1&categoryId=12267&storeId=10051&topCategoryId=12203",
"yoga": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=73463&catalogId=10901&langId=-1&categoryId=73463&storeId=10051&topCategoryId=12203",
"skirts": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=13058&catalogId=10901&langId=-1&categoryId=13058&storeId=10051&topCategoryId=12203",
"dresses": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=12265&catalogId=10901&langId=-1&categoryId=12265&storeId=10051&topCategoryId=12203",
"flipflops": "http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=13056&catalogId=10901&langId=-1&categoryId=13056&storeId=10051&topCategoryId=12203",
"accessories":"http://www.abercrombie.com/webapp/wcs/stores/servlet/CategoryDisplay?parentCategoryId=13060&catalogId=10901&langId=-1&categoryId=13060&storeId=10051&topCategoryId=12203"
}

store = "Abercrombie"

ab = AbercrombieScraper(urls, store)
ab.scrape()
=======
        # save image
        d['filename'] = image.split('/')[-1].split('?$')[0] + '.png'
        urllib.urlretrieve(image, settings.STATIC_ROOT + '/' + d['filename'])
        item = Item(**d)
        item.save()
>>>>>>> e2fa226f3ff807dd1bfcfdba0c4d8c9decbd1c9b
