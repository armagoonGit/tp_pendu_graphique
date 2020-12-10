#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

que fait : fichier qui gere l'affichage graphique du pendu
qui : FOËX Vick 
quand : 10/12/2020
que reste a faire : img, nb de tour, cjhqck victoir
    
"""
from module import getWord
from gameRules import askLettre, genWordUnder, checkPresence, stopGame, endGame, valideLettre 
from tkinter import Tk, Label, Canvas, Button, PhotoImage,StringVar, Entry



def fct(lettreList, lettre,dico ):
    global gWordAff
    
    askLettre(lettreList, lettre, dico)
    gWordAff.pack_forget()
    gWordAff = Label(fen, text = dico["guesWord"], fg='blue')
    gWordAff.pack(side = "top")
    






dico  = {"nbTurn" : 0, "error" : 1, "word": getWord()}
dico["guesWord"] = genWordUnder(dico["word"])
lettreList = [ dico["word"][0] ]
    
fen = Tk()

validBut = Button(fen, text ="Proposer", command = lambda: fct(lettreList, champ.get(),dico ) )
validBut.pack(side = "top")   
       
champ = Entry(fen, textvariable=StringVar())
champ.pack(side="top")


gWordAff = Label(fen, text = dico["guesWord"], fg='blue')
gWordAff.pack(side = "top")

fen.mainloop()


