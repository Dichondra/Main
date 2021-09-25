#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:06:08 2021

@author: franek
"""
import random

def dostępne_ruchy_imp(x,y):
    dost_ruchy = []
    if x + 1 <= 9:
            if y +1 <= 9:
               ruch = [x+1,y+1]
               dost_ruchy.append(ruch)
            if y -1 >=0:
                ruch = [x+1,y-1]
                dost_ruchy.append(ruch)
            ruch = [x+1,y]
            dost_ruchy.append(ruch)
    if x - 1 >= 0:
            if y +1 <= 9:
               ruch = [x-1,y+1]
               dost_ruchy.append(ruch)
            if y -1 >=0:
                ruch = [x-1,y-1]
                dost_ruchy.append(ruch)
            ruch = [x-1,y]
            dost_ruchy.append(ruch)
    if y +1 <= 9:
        ruch = [x,y+1]
        dost_ruchy.append(ruch)
    if y - 1 >= 0:
        ruch = [x,y-1]
        dost_ruchy.append(ruch)
    
    
    
    
    return dost_ruchy

def random_move(x,y):
    los = random.randint(0,1)
    if los == 1:
            x += 1
            if x > 9:
                x -= 2
            
    else:
            x -= 1
            if x < 0:
                x += 2
       
        
    los = random.randint(0,1)
    if los == 1:
            y -= 1
            if y < 0:
                y += 2
    else:
            y += 1
            if y > 9    :
                y -= 2


print(dostępne_ruchy_imp(9, 9))