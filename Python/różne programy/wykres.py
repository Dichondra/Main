# program któremu podane są 3 liczby (a,b,c) gdzie a to kość którą sie rzuca (np 6/10/12/20) b to ilość kości na rzut i c to ile ruztów bierze. Program rzuca c razy
# z ułatwieniem (rzut to rzut b kościami i wybraniem największej) a "a" to kość

import random


def rzut(a,b,c):
    suma = 0
    rzuty = []
    for i in range (c):
        for k in range (b):
            x = random.randint(1,a)
            rzuty.append(x)
        suma += max(rzuty)
        rzuty = []
    suma = suma / c
    return suma


test = 1
for m in range (100):
    print(m," ", end = "")
    print(rzut(20,test,1000))
    test += 1
