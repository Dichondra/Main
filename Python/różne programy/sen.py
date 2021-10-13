#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 13:17:13 2021

@author: franek
"""


# Jest to powrót do pythona z projektem gry sen 

#imports
import random


#zmienne globalne
deck = []


# klasy
class card():
    def __init__(self,numer,power = False):
        self.Numer = numer
        self.power = power
        
    def __str__(self):
        numer = str(self.Numer)
        
        return numer
        
class player():
    def __init__(self):
        self.hand = []
        
    def play(numer):
        pass
    
    
class bot():
    def __init__(self):
        print("Hello i am bot")
        self.hand = []
    
    
#funkcje
        
def Create_deck(deck,card):
    for i in range(9):
        for k in range(4):
            deck.append(card(i))
    for i in range(9):
        deck.append(card(9))
    for i in range(3):
        deck.append(card(5,power=True))
        deck.append(card(6,power=True))
        deck.append(card(7,power=True))
    
def setup_hand(deck,gracz,ilość = 4):
    for i in range(ilość):
        gracz.hand.append(deck[0])
        deck.remove(deck[0])
        
    

#Main
def Main():
    #setup
    Create_deck(deck,card)
    random.shuffle(deck)       
    Asia = player()
    Bot = bot()
    setup_hand(deck,Asia)
    setup_hand(deck,Bot)
    for i in range(len(Asia.hand)):
        print(Asia.hand[i])
        print(Bot.hand[i])
    

    

#Program
Main()



