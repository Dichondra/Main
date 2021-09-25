#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 18:12:47 2021

@author: franek
"""

import random
import curses


movies = open("filmy","r")
tytuły = []
temp_tytuły = []

for line in movies:
    tytuły.append(line)
    
    
def porównanie(list_a,lista_b):
    zwrot = []
    for element in list_a:
        if element in lista_b:
            zwrot.append(element)
    return zwrot
    
class osoba():
    
    def __init__(self):
        self.tura = True
        self.polubione = []
        self.odrzucone = []
    def wybory(self,temp_tytuły):
        wybór = "k"
        for element in temp_tytuły:
            print("Film oceniany to :",element)
            
            while wybór != "y" or "n":
                wybór = input("Czy chcesz dodać ten film do polubionych (y = tak || n = nie : ")
            print(wybór)
            if wybór == "y":
                self.polubione.append(element)
                print("dodany do polubionych")
            if wybór == "n":
                self.odrzucone.append(element)
                print("dodany do odrzuconych")
def Main():
    franek = osoba()
    asia = osoba()
    RUN = True
        
    
    
    while RUN:
        for i in range(10):
            temp_tytuły.append(random.choice(tytuły))
        
        asia.wybory(temp_tytuły)
        print("//////////////////////////")
        print("Teraz jest kolej drugiej osoby")
        franek.wybory(temp_tytuły)
        wynik = porównanie(asia.polubione,franek.polubione)
        if wynik:
            print("Jest match:",wynik)
            RUN = False
        else:
            print("niestety nic nie ma, spróbuję jeszcze raz")
            
Main()