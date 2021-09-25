#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 19:53:58 2021

@author: franek
"""


def solver (lista):
    while lista:
        while 0 in lista:
            lista.remove(0)
        if len(lista) == 0:
            return True
        
        lista.sort(reverse=True)
        
        N = lista.pop(0)
        if N > len(lista):
            return False
            
        for i in range(N):
            lista[i] -= 1
    
    
print(solver([6, 0, 10, 10, 10, 5, 8, 3, 0, 14, 16, 2, 13, 1, 2, 13, 6, 15, 5, 1]))