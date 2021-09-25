#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:25:40 2021

@author: franek
"""

import glob

pos_files = glob.glob("folder/podfolder/train/pos/*.txt")
pos_reviews = []
for file in pos_files:
    with open(file) as stream:
        content = stream.read()
        words = content.lower().replace('<br />'," ").replace("."," " ).split()
        pos_reviews.append(words)
    
neg_files = glob.glob("folder/podfolder/train/neg/*.txt")
neg_reviews = []
for file in neg_files:
    with open(file) as stream:
        content = stream.read()
        words = content.lower().replace('<br />'," ").replace("."," " ).split()
        neg_reviews.append(words)
    
    
### trainin / learning
        
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
        words_sentiment[word] = (pos - neg) / all_
    
# Visualise Words Sentiments
clear = """
sorted_ = sorted(words_sentiment.items(),key = lambda x: x[1])
print("MOST NEGATIVE")
for word, sentiment in sorted_[:10]:
    print(f"* {sentiment:8f} {words_count[word]:6} {word}")
print("MOST POSITIVE")
for word,sentiment in sorted_[:-10]:
    print(f"* {sentiment:8f} {words_count[word]:6} {word}")
    """
def compute_sentiment(words,debug = False):
    sentiment = 0
    for word in words:
        word_sentiment = words_sentiment.get(word, 0)
        word_count = words_count.get(word, 0)
        sentiment += word_sentiment
        if debug == True:
            
            print(word,"word count: ",word_count, "sentiment:",word_sentiment)
        
    sentiment /= len(words)
    return sentiment

n_correct = 0
for review in pos_reviews:
    if compute_sentiment(review) > 0:
        n_correct += 1
for revies in neg_reviews:
    if compute_sentiment(review) < 0:
        n_correct += 1
train_score = n_correct / len(pos_reviews + neg_reviews)

## Testing - interactive
text = " "
while text != "exit":
    text = input("Enter comment: ")
    words = text.lower().replace('<br />'," ").replace("."," " ).split()
    sentiment = compute_sentiment(words,debug = True)
    print("sentiment:",sentiment)