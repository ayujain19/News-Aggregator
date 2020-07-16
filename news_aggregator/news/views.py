from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup

at_r = requests.get("https://edition.cnn.com/world")
at_soup = BeautifulSoup(at_r.content, 'html.parser')
at_headings = at_soup.findAll("h3")
at_headings = at_headings[1:15]
at_news = []
for at in at_headings:
    at_news.append(at.text)

# *************************************8
ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[3:16]
ht_news = []
for hth in ht_headings:
    ht_news.append(hth.text)

# *******************************************
dt_r = requests.get("https://www.bhaskar.com/")
dt_soup = BeautifulSoup(dt_r.content, 'html.parser')
dt_headings = dt_soup.findAll("h3")
dt_headings = dt_headings[1:11]
dt_news = []
for dth in dt_headings:
    dt_news.append(dth.text)

# ********************************************8
bt_r = requests.get("https://www.bbc.com/hindi/international")
bt_soup = BeautifulSoup(bt_r.content, 'html.parser')
bt_headings = bt_soup.findAll("h3")
bt_headings = bt_headings[1:15]
bt_news = []
for bth in bt_headings:
    bt_news.append(bth.text)

def index(request):
    return render(request,'news/index.html', {'at_news':at_news, 'ht_news':ht_news,'dt_news':dt_news, 'bt_news':bt_news})