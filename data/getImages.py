from bs4 import BeautifulSoup
from soupselect import select

#soup = BeautifulSoup('<p class="a">')
#select(soup, '.a')

import urlparse
import html5lib
import html5lib.treebuilders
import urllib
import urllib2
import os
import errno
from top_shop_urls import urls

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

def main():
    #for key in urls.keys():
        #make_sure_path_exists(key)

    for key, value in urls.items():
        fd = urllib2.urlopen(value)
        parsed = BeautifulSoup(fd)
        imgs = parsed.findAll('img', src=lambda s: 'http://mediaus.topshop.com/wcsstore/TopShopUS/images/catalog' in s)
        for img in imgs:
            src = img['src']
            filename = os.path.basename(src).split('_')[0]
            urllib.urlretrieve(src, key + '/' + filename + '_large.jpg')

if __name__ == '__main__':
    main()
