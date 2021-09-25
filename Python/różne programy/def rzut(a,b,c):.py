import random
def rzut(a,b,c):
    # c - ile razy rzucas, b ile kostek na rzut i a to a-ścienna kostka
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

m = 100000
z = 0
for i in range(m):
    x=rzut(20,2,1)
    y = rzut(20,2,1)
    if x < y :
        z += x
    else:
        z += y
    
z = z/m
print(z)
    