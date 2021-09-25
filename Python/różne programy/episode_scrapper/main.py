#!/usr/bin/env python3
# -*-       coding: utf-8 -*-
"""
Created on Wed Aug 18 09:19:42 2021

@author: franek
"""
import urllib.request, smtplib
from second import new_episodes, encode, mail_sender,checker_new_episodes

def Main():
    found = False
    
    page = urllib.request.urlopen("https://www.thewatchcartoononline.tv/anime/boku-no-hero-academia-english-subbed").read()
    page_string = str(page, encode)
    
    checker_new_episodes(new_episodes,page_string)
    if found == True:
       mail_sender()
       
    else:
        print("hello",found, new_episodes)
    
Main()