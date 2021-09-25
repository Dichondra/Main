#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:50:05 2021

@author: franek
"""


from tkinter import *
films = ["a","b","c"]
HEIGHT = 500
WIDTH = 500



class Aplication(Frame):
    def __init__(self,master,films):
        super(Aplication,self).__init__(master)
        self.grid()
        self.create_widgets()
        self.movies = films
        self.odrzucone = []
        self.polubione = []
        self.create_label()
        self.winner = "Tekst"
        
    def create_widgets(self):
        self.bttn1 = Button(self,text = "nie chcę oglądać")
        self.bttn1.grid()
        self.bttn1["command"] = self.dislike
        self.bttn2 = Button(self, text = "Mogę obejrzeć")
        self.bttn2["command"] = self.like
        self.bttn2.grid()
        self.bttn1.grid(row=1,column=1,columnspan =3,sticky = W)
        self.bttn2.grid(row=2,column=2  ,columnspan =3,sticky = W)
        self.bttn3 = Button(self,text = "druga osoba")
        self.bttn3["command"] = self.change
        self.bttn3.grid(row=3,column=3,columnspan=3,sticky=W)
        
    def create_label(self):
        lbl = Label(self,text = self.movies[0])
        lbl.place(x=500,y=500)
        lbl.grid()
        efekt = Label(self,text = "dupa")
        lbl.place(x=100,y=500)
        efekt.grid()
    def dislike(self):  
        self.movies.pop(0)
        self.odrzucone.append(self.movies[0])
        self.create_label()
    def like(self):
        self.movies.pop(0)
        self.polubione.append(self.movies[0])
        self.create_label()
        if len(self.polubione) == len(set(self.polubione)):
            self.winner = self.polubione[-1]
    def change(self):
        self.movies = films
root = Tk()
root.title("Movie Tinder")
root.geometry("500x500")
app = Aplication(root,films)
root.mainloop()