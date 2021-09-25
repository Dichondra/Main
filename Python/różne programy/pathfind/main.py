#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 16:22:46 2021

@author: franek
"""

import random
from imports import *
from time import sleep

X = 10




class board():
    
    def __init__(self,x):
        self.szachownica = []
        self.x = x
        for i in range(self.x):
            lista = []
            for i in range(self.x):
                lista.append(False)
            
            self.szachownica.append(lista)
            
            
class punkt():
    
    def __init__(self):
        self.x = random.randint(0,X-1)
        self.y = random.randint(0,X-1)


class ludzik():
    
    def __init__(self,punkt,board):
        # generowanie współrzędnych
        self.x = random.randint(0,X-1)
        self.y = random.randint(0,X-1)
        while self.x == punkt.x and self.y != punkt.y:
           self.x = random.randint(0,X-1)
           self.y = random.randint(0,X-1)  
        board.szachownica[self.y][self.x] = True
        
    def move(self):
        self.dostępne_ruchy = dostępne_ruchy_imp(self.x,self.y)

        
        for ruch in self.dostępne_ruchy:
            if board.szachownica[ruch[0]][ruch[1]] == False:
                self.x = ruch[0]
                self.y = ruch[1]
                
                board.szachownica[self.x][self.y] = True
            else:
                pass
        print("bot: ",self.x,self.y)
            
        # zbiera listę wszystkich sąsiednich pól i ich wartości 
        # losuje z wartości false
        # jeśli nie może to losuje z wartości true
        # zmienia swój x i y na odpowiadajace 
    ### to do : generowanie ruchu i zmiana współrzędnych szachownicy na True
    
        
            



board = board(X) #tworzę szachownicę o x^2 polach
dot = punkt()
bot = ludzik(dot,board)




print("dot: ",dot.x,dot.y)
print("bot : ",bot.x,bot.y)
while board.szachownica[dot.x][dot.y] == False:
    bot.move()
    sleep(1)
for i in range(10):
        print(board.szachownica[i])
print("sukcess")
print(bot.x,bot.y)