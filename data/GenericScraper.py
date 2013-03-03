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

<<<<<<< HEAD
class GenericScraper:
=======
class GenericScraperClass:
    # subclasses must define
    urls = {}
    type_mapping = {}
    high_level_category_mapping = {}
>>>>>>> e2fa226f3ff807dd1bfcfdba0c4d8c9decbd1c9b

    urls = {}
    
    def __init__(self, urls):
        self.urls = urls

    def scrape(self):
        for category in self.urls.keys():
            self.scrapeCategory(category)

    def scrapeCategory(self, category):
        # read page using beautiful soup
        fd = urllib2.urlopen(self.urls[category])
        parsed = BeautifulSoup(fd)

        # isolate items
        items = self.findItems(parsed)
<<<<<<< HEAD

        # process Items
        for item in items:
=======
        
        for item in items:
            # processItem
>>>>>>> e2fa226f3ff807dd1bfcfdba0c4d8c9decbd1c9b
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

<<<<<<< HEAD
    def processItem(self, parsed, item):
=======
    def processItem(self, parsed, item, itemCategory):
>>>>>>> e2fa226f3ff807dd1bfcfdba0c4d8c9decbd1c9b
        # get image, save
        # set store
        # get title, price, description, price, color, keywords
        # set type and high_level_category using dicts from models.py
        raise "Method not implemented"
