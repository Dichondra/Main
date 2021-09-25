#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:34:12 2021

@author: franek
"""


import glob

pos_files = glob.glob("folder/podfolder/train/pos/*.txt")
pos_reviews = []
for file in pos_files:
    with open(file) as stream:
        content = stream.read()
        words = content.lower().replace('<br />', " ").replace("."," " ).split()
        pos_reviews.append(words)
    
neg_files = glob.glob("folder/podfolder/train/neg/*.txt")
neg_reviews = []
for file in neg_files:
    print("H")
    with open(file) as stream:
        content = stream.read()
        words = content.lower().replace('<br />'," ").replace("."," " ).split()
        neg_reviews.append(words)
    

words_count = {}
words_count_pos = {}
words_count_neg = {}

for review in pos_reviews:
    for word in set(review):
        words_count[word] = words_count.get(word, 0) + 1
        words_count_pos[word] = words_count_pos.get(word, 0) + 1

for review in neg_reviews:
    for word in set(review):
        words_count[word] = words_count.get(word, 0) + 1
        words_count_neg[word] = words_count_neg.get(word, 0) + 1
             

words_sentiment = {}
for word in words_count.keys():
    if words_count[word] >= 50:
        pos = words_count_pos.get(word, 0)
        neg = words_count_neg.get(word,0)
        all_ = words_count[word]
        words_sentiment[word] = (pos-neg)/all_
        
 