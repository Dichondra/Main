#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:56:54 2021

@author: franek
"""


### Gra w dedukcję. Komputer losuje 3 cyforową liczbę. Gracz próbuję ją zgadnąć
### jeśli żadna cyfra się nie pojawia komputer mówi : Bagles
### jeśli jest cyfra ale nie na dobrym miejscu mówi : Pico
### jeśli jest cyfa i na dobrym miejscu mówi : Fermi


import random 
from różne import *



def Guess():
   
    strzał = []
    anwser = str(input("W jaką liczbę strzelasz: "))
    for number in anwser:
        number = int(number)
        strzał.append(number)
    return(strzał)
   


def Main():
    tekst()
    x = random.randint(100,999)
    x = str(x)
    liczba = []
    count = 0
    for number in x:
        number = int(number)
        liczba.append(number)
    anwser = []
    
    odpowiedź = []
    while anwser != liczba:
        anwser = Guess()
        copy = liczba[:]
        for i in range(3):
            if anwser[i] == liczba[i]:
                odpowiedź.append("Fermi")
                
            if anwser[i] in copy and anwser[i] != liczba[i]:
                odpowiedź.append("Pico")
                copy.remove(anwser[i])
        
        if anwser[0] not in liczba and anwser[1] not in liczba and anwser[2] not in liczba:
            odpowiedź.append("Bagle")
            
        copy = liczba[:]
        odpowiedź.sort()
        print(odpowiedź)
        odpowiedź = []
        count += 1
    
    print("Gratuluję zgadłeś, a potrzebowałeś do tego ", count, "prób")
        
        
        
Main()