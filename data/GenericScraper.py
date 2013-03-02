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

class GenericScraper:

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
