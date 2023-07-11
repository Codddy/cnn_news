import feedparser
from tkinter import *

url = "http://rss.cnn.com/rss/edition.rss"
news = feedparser.parse(url)

for new in news.entries:
    print(new.title)
    print(new.link)