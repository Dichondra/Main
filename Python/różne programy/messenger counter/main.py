#!/r/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 23:22:13 2021

@author: franek
"""
import json,os.path
#słownik ze słowami i ich ilością
słownik = {}

# główna funkcja ukladająca słowa do słownika 
def Main(data):
    for message in data["messages"]:
        if message["sender_name"] == "Asia Wid\u00c5\u0082a":
            try :
                message = message["content"].lower().replace("."," ").split(" ")
                
            except:
                pass
            for word in message:
                if len(word) >= 5:
                    słownik[word] = słownik.get(word, 0 ) + 1






            


            
for i in range(1):
    x = str(i+1)
    lista = ["message_",x,".json"]
    file_name = "".join(lista)
    file = os.path.join("/home/franek/Desktop/big_files_github/Asiula",file_name)
    f = open(file)
    data = json.load(f)
    Main(data)
    f.close()

ułożony = sorted(słownik.items(), key=lambda x: x[1])
print(ułożony)
print(len(ułożony))