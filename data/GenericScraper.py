from bs4 import BeautifulSoup
from soupselect import select
import urlparse
import html5lib
import html5lib.treebuilders
import urllib
import urllib2
import os
import errno

class GenericScraper:
    # subclasses must define
    urls = []
    type_mapping = {}
    high_level_category_mapping = {}

    store = "Unknown"

    def scrape:
        for url in urls:
            scrapeUrl(url)

    def scrapeUrl(url):
        # read page using beautiful soup
        fd = urllib2.urlopen(url)
        parsed = BeautifulSoup(fd)

        # isolate items
        items = findItems(parsed)

        for item in items:
            # processItem
            fd = urllib2.urlopen(item[0])
            parsed = BeautifulSoup(parsed)
            processItem(parsed, item)

    # subclasses must define
    # takes in page parsed by beautiful soup and produces 
    # a list of item (url + possibly some metadata), i.e.
    # produces a list of tuples. Assume that the first entry
    # in list is the url
    def findItems(parsed):
        # items = []
        # find item urls and metadata
        # return items
        raise "Method not implemented"

    def processItem(parsed, item):
        # get image, save
        # get title
        # get price
        # get color
        # get metadata
        # create item in database and save
        raise "Method not implemented"
