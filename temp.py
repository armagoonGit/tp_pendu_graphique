# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from module import getWord
from gameRules import askLettre, genWordUnder, checkPresence, stopGame, endGame, valideLettre 
from tkinter import Tk, Label, Canvas, Button, PhotoImage,StringVar, Entry, Toplevel

class fentre():
    def __init__(self):
        self.fen = Tk()
        self.dico = {"nbTurn" : 0, "error" : 1, "word": getWord()}
        self.lettreList = [ dico["word"][0] ]
        self. dico["guesWord"] = genWordUnder(self.dico["word"])
    
        
        self.valideBut = Button(self.fen, text="Proposer", command=lambda:self.change() )
        self.champ = Entry(self.fen, textvariable="oui")
        self.gWordAff = Label(self.fen, text=self.dico["guesWord"], fg='blue')
        
        self.img = PhotoImage(file="image/bonhomme1.gif")
        self.can = Canvas(self.fen, width= 300, height= 300)

        
    def go(self):
        self.can.create_image(0,0,anchor="nw", image=self.img)
        self.can.pack(side="right")
        self.valideBut.pack(side="top")
        self.champ.pack(side="top")
        self.gWordAff.pack(side="top")

        self.fen.mainloop()

    def change(self):

         askLettre(self.lettreList, self.champ.get() , self.dico)
         print(self.dico)
         
         self.img = PhotoImage(file="image/bonhomme" + str(self.dico["error"]) +".gif")
         self.gWordAff.config(image=self.img)
         self.gWordAff.pack(side='right')
         
         self.gWordAff.config(text=self.dico["guesWord"])
         
         
         

         
         
        
        

a = fentre()
a.go()


