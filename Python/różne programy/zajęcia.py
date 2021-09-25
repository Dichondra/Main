#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 11:05:32 2021

@author: franek
"""


import random

zajęcia = ["czytać","grać w szachy","uczyć się szachów","poezja (nauka/czytanie)","nauka rysunku","spacer",
           "nauka programowania","programowanie","nauka języka","nauka na studia","pisać świat do dnd",
           "medytacja","sprzątanie","journal"]
czas = ["15","30","45"]

def Main():
    temp_zajęcia = []
    for zajęcie in zajęcia:
        print("W skalie 1-10 (gdzie 10 to najbardziej 1 to najmniej, jak bardzo chcesz wykonać podaną aktywność ",zajęcie)
        skala = int(input("Moja odpowiedź to: "))
        for i in range(skala):
            temp_zajęcia.append(zajęcie)
    input("Obiecuje że wykonam te 3 zajęcia tak jak zostały wylosowane dla mnie :")
    for i in range(10):
        act = random.choice(temp_zajęcia)
        print(i+1,"zajęcie które robisz to : ",act)
        while act in temp_zajęcia:
            temp_zajęcia.remove(act)
        y = random.choice(czas)
        #czas.remove(y)
        print("Czas trwania tego zajęcia to :",y)

Main()