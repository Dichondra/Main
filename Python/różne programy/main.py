#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:22:46 2021

@author: franek
"""

import random
from imports.py import *

X = 10




class board():
    def __init__(self,x):
        self.LENGTH = x
        self.szachownica = []
        lista = []
        for i in range(x):
            lista.append(False)
        for i in range(x):
            self.szachownica.append(lista)
            
class punkt():
    def __init__(self):
        self.x = random.randint(0,X-1)
        self.y = random.randint(0,X-1)


class ludzik():
    def __init__(self,punkt):
        # generowanie współrzędnych
        self.x = random.randint(0,X-1)
        self.y = random.randint(0,X-1)
        while self.x == punkt.x and self.y != punkt.y:
           self.x = random.randint(0,X-1)
           self.y = random.randint(0,X-1)  
         
    def move(self):
        
        self.dostępne_ruchy

        # zbiera listę wszystkich sąsiednich pól i ich wartości 
        # losuje z wartości false
        # jeśli nie może to losuje z wartości true
        # zmienia swój x i y na odpowiadajace 
    ### to do : generowanie ruchu i zmiana współrzędnych szachownicy na True
    def dostępne_ruchy(self):
        dostępne_ruchy_imp(self.x,self.y)
        
            



board = board(X)
dot = punkt()
bot = ludzik(dot)
print(dot.x,dot.y)
print(bot.x,bot.y)