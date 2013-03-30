import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
from optparse import make_option
from django.core.management.base import NoArgsCommand, make_option
from data.TopshopScraper import *

class Command(NoArgsCommand):

    help = "scrape website and write to DB"

    option_list = NoArgsCommand.option_list + (
        make_option('--verbose', action='store_true'),
    )

    def handle_noargs(self, **options):
        # call script here
	print "Test"
	TopshopScraperClass().scrape()
	print "Done"
