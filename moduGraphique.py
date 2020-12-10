# -*- coding: utf-8 -*-
"""
que fait : fichier module du projet pendu avec interface
qui : FOËX Vick 
quand : 10/12/2020
que reste a faire : ajout anex
"""

from tkinter import Tk, Label, Canvas, Button, PhotoImage, Entry

from module import getWord, adaptGuesWord
from gameRules import askLettre, genWordUnder

class fentre():
    def __init__(self):
        #variables simple
        self.dico = {"nbTurn" : 0, "error" : 1, "word": getWord(), "message":"rien"}
        self.lettreList = [ dico["word"][0] ]
        self. dico["guesWord"] = genWordUnder( self.dico["word"] )
    
        #tkinter
        self.fen = Tk()
        self.valideBut = Button( self.fen, text = "Proposer", command = lambda : self.change() )
        self.fatal = Button( self.fen, text = "tricher", command = lambda : self.fatalEnd() )
        
        self.champ = Entry( self.fen, textvariable = "non")
        
        self.gWordAff = Label( self.fen, text = adaptGuesWord( self.dico["guesWord"] ) )
        self.message =Label( self.fen, text = "Tapez une lettre")
        
        self.img = PhotoImage( file="image/bonhomme1.gif" )
        self.can = Canvas( self.fen, width = 300, height = 300 )

        
    def go(self): #mise en place au debut du programe
        self.fen.title("Jeu du pendu")
        
        self.gWordAff.grid(row = 1, column = 2)
        
        self.valideBut.grid(row = 2, column = 1)
        self.champ.grid(row = 2, column = 2)
        self.champ.focus_set()
        
        self.message.grid(row= 3, column = 2)
        self.fatal.grid(row= 3, column = 1)
        
        self.can.create_image(0,0,anchor="nw", image=self.img)
        self.can.grid(row = 1, column = 3, rowspan= 3)

        self.fen.mainloop()


    def change(self): #actualisation qd on soument une lettre
         askLettre(self.lettreList, self.champ.get() , self.dico)
         self.champ.delete( 0, "end" )
         
         if self.dico["error"] == 8:
             self.end()
         
         self.gWordAff.config( text =  adaptGuesWord( self.dico["guesWord"] ) )
         self.message.config( text = self.dico["message"] )
         
         self.can.delete("all")
         self.img = PhotoImage( file="image/bonhomme" + str( self.dico["error"]) + ".gif" )
         self.item = self.can.create_image( 0, 0, anchor="nw", image=self.img )


    def end(self):
        self.dico["message"] = "desoler c'est perdu, le mots etait: " + self.dico["word"]
        self.valideBut.destroy()
        
    def fatalEnd(self):
        self.dico["message"] = "Che"
        self.message.config( text = self.dico["message"] )
        self.valideBut.destroy()
        
        
         
         
         

a = fentre()
a.go()


