#!/usr/bin/env python

import sys
from nypost_scraper import scrape_page

# Going to parse the data directly from NY Post...


scrape_page("https://nypost.com/sports/", "nba")
