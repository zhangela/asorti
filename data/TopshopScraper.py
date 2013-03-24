from GenericScraper import *
#import requests
from HTMLParser import HTMLParser

class TopshopScraperClass(GenericScraperClass):


    # TODO!!!
    type_mapping = {'tops' : 'tops', 
                    'dresses-1' : 'dresses', 
                    'dresses-2' : 'dresses', 
                    'coats' : 'outerwear', 
                    'denim' : 'pants', 
                    'jackets' : 'outerwear', 
                    'jeans' : 'jeans',
                    'jersey-tops-1' : 'tops',
                    'jersey-tops-2' : 'tops',
                    'knitwear' : 'tops',
                    'leggings' : 'leggings-pants',
                    'pants' : 'pants',
                    'rompers' : 'dresses',
                    'shorts' : 'shorts',
                    'skirts' : 'skirts',
                    'suits-coords' : 'tops',
                    'tights-socks' : 'tights',
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
        d ['store'] = self.store
        d['url'] = item
        d['type'] = type[self.type_mapping[itemCategory]]
        d['high_level_category'] = high_level_category[type_to_high_level_category[self.type_mapping[itemCategory]]]
        d['description'] = parsed.find('p', class_='product_description').getText()
        d['keywords'] = ""
        d['title'] = parsed.find('h1').getText()
        image = parsed.find('a', class_="product_view").get('href')

        d['price'] = parsed.find('li', class_='product_price').find('span').getText().replace("$", "")
        d['color'] = parsed.find('li', class_='product_colour').find('span').getText().title()
        

        # save image
        d['filename'] = image.split('/')[-1].split('?$')[0] + '.png'
        #TODO: temporarily commented out: figure out file upload in apache
    #urllib.urlretrieve(image, settings.STATIC_ROOT + '/' + d['filename'])
        item = Item(**d)
        item.save()
