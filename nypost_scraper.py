import sys
import urllib2
from bs4 import BeautifulSoup

'''
Parse HTML of NY Post 
'''
def scrape_page(path, sport):

    with open(path, 'r') as testFile:
        doc = testFile.read();

    parsed_data = BeautifulSoup(doc, 'html.parser')

    # Grab the lines div
    parent_tag = parsed_data.find_all("div", { "class": "box no-mobile module widget_nypost_post_line_widget"})



    print len(parent_tag)

