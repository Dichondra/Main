#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:06:16 2021

@author: franek
"""


#### testowu 
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


X = 10


class dot():
    def __init__(self):
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
        print("jestem punktem ze współrzędnymi :",self.x,self.y)
        
        
    def change(self):
        self.x = random.randint(0,9)
        self.y = random.randint(0,9)
class board():
    
    def __init__(self,x):
        self.szachownica = []
        self.x = x
        for i in range(self.x):
            lista = []
            for i in range(self.x):
                lista.append(False)
            
            self.szachownica.append(lista)
        
    def change(self):
        self.szachownica = []
        
        for i in range(self.x):
            lista = []
            for i in range(self.x):
                lista.append(False)
            
            self.szachownica.append(lista)
class ludzik():
    
    def __init__(self,punkt,board):
        # generowanie współrzędnych
        self.x = random.randint(0,X-1)
        self.y = random.randint(0,X-1)
        while self.x == punkt.x and self.y != punkt.y:
           self.x = random.randint(0,X-1)
           self.y = random.randint(0,X-1)  
        board.szachownica[self.y][self.x] = True
        self.kroki = 0
        print("bot położenie :",self.x,self.y)
    def move(self):
        count = 0
        self.dostępne_ruchy = dostępne_ruchy_imp(self.x,self.y)
        
        for ruch in self.dostępne_ruchy:
            if board.szachownica[ruch[0]][ruch[1]] == False:
                self.x = ruch[0]
                self.y = ruch[1]
                board.szachownica[ruch[0]][ruch[1]] = True
                self.kroki += 1
                break
            else:
                count += 1
            if count == len(self.dostępne_ruchy):
                ruch = random.choice(self.dostępne_ruchy)
                self.x = ruch[0]
                self.y = ruch[1]
                board.szachownica[ruch[0]][ruch[1]] = True  
                self.kroki += 1
            print("bot: ",self.x,self.y)
    
    def change(self):
        self.x = random.randint(0,X-1)
        self.y = random.randint(0,X-1)
        while self.x == punkt.x and self.y != punkt.y:
           self.x = random.randint(0,X-1)
           self.y = random.randint(0,X-1)
        self.kroki = 0
punkt = dot()          
board = board(X)
bot = ludzik(punkt,board)


def Main(M):
    average = 0
    for i in range(M):
        punkt.change()
        board.change()
        bot.change()
        while not board.szachownica[punkt.x][punkt.y]:
            bot.move()
        average += bot.kroki
    average = average / M
    return average

print(Main(1))
    