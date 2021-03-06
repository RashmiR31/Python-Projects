# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:30:27 2021

@author: Rashmi R
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyshorteners

url = "https://news.google.com/news/rss"
client = urlopen(url)
xml_data = client.read()
client.close()

soup = BeautifulSoup(xml_data,'xml')
news_list = soup.find_all('item')
news_list = news_list[0:5]
s=pyshorteners.Shortener()

for news in news_list:
    print(news.title.text)
    old_link = news.link.text
    new_link = s.tinyurl.short(old_link)
    print(new_link)
    print(news.pubDate.text)
    print("-"*20)
    