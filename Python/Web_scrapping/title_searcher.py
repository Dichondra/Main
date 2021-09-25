#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 11:17:26 2021

@author: franek
"""



from bs4 import BeautifulSoup as Soup
import requests


url = "https://www.imdb.com/chart/top/"

page = requests.get(url)

doc = Soup(page.text,"html.parser")


titles = doc.find_all(class_ = "titleColumn")



tytuły = []

for title in titles:
    title = title.find("a")
    title = title.string
    tytuły.append(title)
    

f = open("filmy","a")

for element in tytuły:
    f.write(element)
    f.write("\n")
f.close()

