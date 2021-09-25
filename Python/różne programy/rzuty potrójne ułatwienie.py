import random

def normal(n):
    rzuty2 = 0
    for i in range(n):
        x = random.randint(0,20)
        rzuty2 += x
    zwrot = rzuty2 / n
    print(zwrot)

def ułat_two(n):
    rzuty = 0
    rzut = []
    for i in range (n):
        
        b = random.randint(0,20)
        c = random.randint(0,20)
        
        rzut.append(b)
        rzut.append(c)

        rzuty += max(rzut)
        rzut = []
    value = rzuty / n
    print(value)



def ułat_three(n):
    rzuty = 0
    rzut = []
    for i in range (n):
        a = random.randint(0,20)
        b = random.randint(0,20)
        c = random.randint(0,20)
        rzut.append(a)
        rzut.append(b)
        rzut.append(c)
        rzuty += max(rzut)
        rzut = []
    value = rzuty / n
    print(value)

def ułat_test(n):
    rzuty = 0
    rzut = []
    for i in range (n):
        a = random.randint(0,20)
        b = random.randint(0,20)
        c = random.randint(0,20)
        d = random.randint(0,20)
        e = random.randint(0,20)
        rzut.append(a)
        rzut.append(b)
        rzut.append(c)
        rzut.append(d)
        rzut.append(e)
        rzuty += max(rzut)
        rzut = []
    value = rzuty / n
    print(value)

def alls(n):
    normal(n)
    ułat_two(n)
    ułat_three(n)
    

ułat_test(100000)