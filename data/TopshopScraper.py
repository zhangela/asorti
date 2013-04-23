from pyvirtualdisplay import Display
from GenericScraper import *
import requests
from HTMLParser import HTMLParser
from pprint import pprint

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

class TopshopScraperClass(GenericScraperClass):

    # TODO!!!
    type_mapping = {'tops' : 'tops',
    'dresses-1' : 'dresses',
    'dresses-2' : 'dresses',
    'coats' : 'outerwear',
    'denim' : 'leggings-pants',
    'jackets' : 'outerwear',
    'jeans' : 'jeans',
    'jersey-tops-1' : 'tops',
    'jersey-tops-2' : 'tops',
    'knitwear' : 'tops',
    'leggings' : 'leggings-pants',
    'pants' : 'leggings-pants',
    'rompers' : 'dresses',
    'shorts' : 'shorts',
    'skirts' : 'skirts',
    'suits-coords' : 'tops',
    #'tights-socks' : 'tights',
    'bags-and-purses' : 'accessories',
    'belts' : 'accessories',
    'collars' : 'accessories',
    'hats' : 'accessories',
    'scarves' : 'accessories',
    'winter-accessories' : 'accessories',
    'jewelry-1' : 'accessories',
    'jewelry-2' : 'accessories',
    'umbrellas' : 'accessories',
    'sunglasses' : 'accessories',
    'heels' : 'shoes',
    'flats' : 'shoes',
    'boots' : 'shoes',
    'premium-shoes' : 'shoes'
    }

    store = "Topshop"

    urls = {
           'tops' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208637&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208637&parent_categoryId=208580&beginIndex=1&pageSize=500',
           'dresses-1' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208634&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208634&parent_categoryId=208580&beginIndex=1&pageSize=500',
           'dresses-2' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208634&parent_categoryId=208580&beginIndex=201&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208634&parent_categoryId=208580&beginIndex=201&pageSize=500',
           'coats' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=674426&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=674426&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'denim' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=525520&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=525520&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'jackets' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208640&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208640&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'jeans' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208641&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208641&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'jersey-tops-1' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=230162&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=230162&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'jersey-tops-2' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=230162&parent_categoryId=208580&beginIndex=201&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=230162&parent_categoryId=208580&beginIndex=201&pageSize=200',
           'knitwear' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208638&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208638&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'leggings' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=928191&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=928191&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'pants' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208642&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208642&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'rompers' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208652&parent_categoryId=208580&beginIndex=1&pageSize=20&intcmpid=W_SUPERCAT_LEFTNAV_CLOTHING_US_WK1_PLAYSUITS#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208652&parent_categoryId=208580&beginIndex=1&pageSize=200&intcmpid=W_SUPERCAT_LEFTNAV_CLOTHING_US_WK1_PLAYSUITS',
           'shorts' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208645&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208645&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'skirts' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208649&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208649&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'suits-coords' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=423014&parent_categoryId=208580&beginIndex=1&pageSize=500',
           'tights-socks' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208656&parent_categoryId=208580&beginIndex=1&pageSize=500#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208656&parent_categoryId=208580&beginIndex=1&pageSize=200',
           'bags-and-purses' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208705&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208705&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'belts' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208711&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208711&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'collars' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=444657&parent_categoryId=208582&beginIndex=1&pageSize=20',
           'hats' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208708&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208708&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'scarves' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208710&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208710&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'winter-accessories' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=625179&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=625179&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'jewelry-1' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208714&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208714&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'jewelry-2' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208714&parent_categoryId=208582&beginIndex=201&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208714&parent_categoryId=208582&beginIndex=201&pageSize=200',
           'umbrellas' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=false&sort_field=Relevance&categoryId=208712&parent_categoryId=208582&beginIndex=1&pageSize=20',
           'sunglasses' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208713&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208713&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'hair-accessories' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208709&parent_categoryId=208582&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208709&parent_categoryId=208582&beginIndex=1&pageSize=200',
           'heels' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208692&parent_categoryId=208581&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208692&parent_categoryId=208581&beginIndex=1&pageSize=200',
           'flats' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208694&parent_categoryId=208581&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208694&parent_categoryId=208581&beginIndex=1&pageSize=200',
           'boots' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208695&parent_categoryId=208581&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=208695&parent_categoryId=208581&beginIndex=1&pageSize=200',
           'premium-shoes' : 'http://us.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationSearchResultCmd?catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=330540&parent_categoryId=208581&beginIndex=1&pageSize=200#catalogId=33060&storeId=13052&langId=-1&viewAllFlag=true&sort_field=Relevance&categoryId=330540&parent_categoryId=208581&beginIndex=1&pageSize=200'
           }





    def __init__(self):
      self.display = Display(visible=0, size=(1024, 768))
      self.display.start()
      self.browser = webdriver.Firefox()
      actions = webdriver.ActionChains(self.browser)
      self.rec_items_urls = open("temp_rec_items.txt", 'w')

    # takes in page parsed by beautiful soup and produces
    # a list of item (url + possibly some metadata), i.e.
    # produces a list of tuples. Assume that the first entry
    # in list is the url
    def findItems(self, parsed):
      print "finding items"
      items = []

      sp5_div = parsed.find_all('div', attrs={'class': "sp_5"})
      product_div = [line for line in sp5_div if "sp_5 block_" in str(line)]

      for product in product_div:
        items.append(product.find('a').get('href'))

      return items


    def processItem(self, parsed, item, itemCategory):

      d = {}
      d['store'] = self.store
      d['url'] = item
      d['type'] = type[self.type_mapping[itemCategory]]
      d['high_level_category'] = high_level_category[type_to_high_level_category[self.type_mapping[itemCategory]]]
      d['description'] = parsed.find('p', class_='product_description').getText() if parsed.find('p', class_='product_description') else ""
      d['keywords'] = ""
      d['title'] = parsed.find('h1').getText() if parsed.find('h1') else ""
      d['price'] = parsed.find('li', class_='product_price').find('span').getText().replace("$", "") if parsed.find('li', class_='product_price') and parsed.find('li', class_='product_price').find('span') else -1
      d['color'] = parsed.find('li', class_='product_colour').find('span').getText().title() if parsed.find('li', class_='product_colour') else ""

      # process similar items
      associated_product_urls = []
      associated_products = parsed.findAll('div', class_="associated_product")
      if associated_products:
        for product in associated_products:
          associated_product_urls.append(str(product.find('a', class_="product_image").get('href')).split("/")[-1].replace("small", "large"))


      # process images
      image = parsed.find('a', class_="product_view").get('href') if parsed.find('a', class_="product_view") else None
      # save image
      filename = image.split('/')[-1].split('?$')[0] if image else None
      print filename
      if filename:
        self.rec_items_urls.write(filename +":" + str(associated_product_urls) + "\n")
        if len(Item.objects.filter(filename=filename)) == 0:
          print settings.STATIC_ROOT
          # print settings.STATICFILES_DIRS + '/' + filename
          urllib.urlretrieve(image, settings.STATIC_ROOT + '/' + filename)
          d['filename'] = filename
          item = Item(**d)
          item.save()
        else:
          Item.objects.filter(filename=filename).update(**d)

    def scrape(self):
        for category in self.urls.keys():
            	self.scrapeCategory(category)
        self.browser.quit()
        display.stop()
        self.rec_items_urls.close()
        self.rec_items_urls = open("temp_rec_items.txt", 'r')
	      # go through rec_items dict and add to ScrapedRecommendations
        for line in self.rec_items_urls:
          parts = line.split(":")
          item1 = Item.objects.get(filename=part[0])
          for rec_item in parts[1].split('[')[1].split(']')[0].split(','):
            item2 = Item.objects.get(filename=rec_item)
          newScrapedRecommendation = ScrapedRecommendations(item=item1, rec_item=item2)
          newScrapedRecommendation.save()
        self.rec_items_urls.close()


    def scrapeCategory(self, category):
        # read page using beautiful soup
        fd = requests.get(self.urls[category]).content
        parsed = BeautifulSoup(fd, 'html.parser')

        # isolate items
        items = self.findItems(parsed)

        for item in items:
            # processItem
            self.browser.get(item)
            content = self.browser.page_source
            parsed = BeautifulSoup(content)
            self.processItem(parsed, item, category)



## for testing
    # def scrapeItem(self, item_url):

    #   self.browser.get(item_url)
    #   content = self.browser.page_source
    #   self.browser.quit()

    #   parsed = BeautifulSoup(content)

    #   category = "dresses-1"
    #   self.processItem(parsed, item_url, category)

# scraper = TopshopScraperClass()
# scraper.scrape()


