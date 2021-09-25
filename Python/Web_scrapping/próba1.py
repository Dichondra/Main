#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:43:29 2021

@author: franek
"""


import requests, bs4
lista = []



res = requests.get("https://www.imdb.com/chart/top/")
res.raise_for_status
imbdSoup = bs4.BeautifulSoup(res.text,'html.parser')


elems = imbdSoup.find(".titleColumn")
elems = elems.string


for element in elems:
    element = str(element)
    elemt = element[90:-50]
    lista.append(elemt)
    
    
print(lista)