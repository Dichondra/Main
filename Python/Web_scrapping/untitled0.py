#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 15:50:48 2021

@author: franek
"""



### tworzy planszę o wymiarach x na y 
### umieszcza punkt na tej planszy 
### umieszcza ludka na tej planszy
### ludzik chodzi losowo, liczone są jego kroki
### jak ludzik wejdzie na punkt gra się kończy i printuje ile kroków było wykonanych

import random
from time import sleep


x = 10
y = 10


class punkt():
    def __init__(self,x,y):
        self.x = random.randint(1,x)
        self.y = random.randint(1,y)
        
class ludzik():
    def __init__(self,punkt,x,y):
        self.x = random.randint(1,x)
        self.y = random.randint(1,y)
        self.run = True
        self.steps = 0

        while self.x == punkt.x and self.y == punkt.y:
            self.x = random.randint(1,x)
            self.y = random.randint(1,y)
    
    def move(self,punkt):
        los = random.randint(0,1)
        if los == 1:
            self.x += 1
            if self.x > 10:
                self.x -= 2
            
        else:
            self.x -= 1
            if self.x <1:
                self.x += 2
       
        
        los = random.randint(0,1)
        if los == 1:
            self.y -= 1
            if self.y <1:
                self.y += 2
        else:
            self.y += 1
            if self.y > 10:
                self.y -= 2
        self.steps +=1
        
        if self.x == punkt.x and self.y == punkt.y:
            print("koniec gry. Potrzebowałem",self.steps,"ruchów")
            self.run = False
        self.change_run()
    
    def change_run(self):
        if not self.run:
            return self.run
   
        
        
        

dot = punkt(x,y)
bot = ludzik(dot,x,y)
print(dot.x,dot.y)
while bot.run:
    print(bot.x,bot.y)
    bot.move(dot)
    print(bot.run)
