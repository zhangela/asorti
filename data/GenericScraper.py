from bs4 import BeautifulSoup
from soupselect import select
import urlparse
import html5lib
import html5lib.treebuilders
import urllib
import urllib2
import os
import errno

class GenericScraperClass:
    # subclasses must define
    urls = {}
    type_mapping = {}
    high_level_category_mapping = {}

    store = "Unknown"

    def scrape(self):
	print len(self.urls.keys())
        for category in self.urls.keys():
            self.scrapeCategory(category)
	    break

    def scrapeCategory(self, category):
        # read page using beautiful soup
	print "urllibed before"
        fd = urllib2.urlopen(self.urls[category])
	print "urllibed"
        parsed = BeautifulSoup(fd, 'html.parser')
	print "bsed"
        
	# isolate items
        items = self.findItems(parsed)
	print "items found"

        for item in items:
            # processItem
            fd = urllib2.urlopen(item)
            parsed = BeautifulSoup(fd, 'html.parser')
            self.processItem(parsed, item, category)
	    return
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

    def processItem(self, parsed, item, itemCategory):
        # get image, save
        # set store
        # get title, price, description, price, color, keywords
        # set type and high_level_category using dicts from models.py
        raise "Method not implemented"
