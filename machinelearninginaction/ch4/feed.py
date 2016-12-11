import feedparser
import json
ny = feedparser.parse("http://newyork.craigslist.org/search/stp?format=rss")
print ny