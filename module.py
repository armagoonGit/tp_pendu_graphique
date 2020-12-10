#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
que fait : fichier module du projet pendu avec interface
qui : FOËX Vick 
quand : 10/12/2020
que reste a faire: non
    
"""

from random import randint


def readWord():
    wordDoc = open('liste_mot.txt')
   
    wordList = []
    for el in wordDoc :
        wordList.append( el.rstrip('\n') )
        
    wordDoc.close() 
    return(wordList)

def sortList(wordList):
    """
    Trie une liste par taille de mot. et par ordre alphabetique
    return : la liste trier 
    """

    sieze = {}
    wordList.sort()

    for el in wordList :
        lenEl = str( len( el ) )
        
        if lenEl in sieze: 
            sieze[ lenEl ].append( el )
        else:
            sieze[ lenEl ] = [el]
            
    key =sorted( list( sieze.keys() ) )
    wordList = []
    for k in key:
        wordList += sieze[k]
    
    return(wordList)

def pickWord(wordList):
    """
    renvoie une mot aletatoire dans un liste de mot passer en para
    """

    rand = randint(0, len( wordList ) - 1 )
    return( wordList[ rand ].upper() )
    

def getWord():
    """
    renvoie un mot aleatoire du fichier de mot
    """
    
    wordList = readWord()
    wordList = sortList(wordList)
    word = pickWord(wordList)
    return( word )
    
def addLettre(guesWord, lettre, index):
    """
    concatenation d'une str pour changer un char a l'index demander
    """
    guesWord = guesWord[:index] + lettre + guesWord[index + 1:]
    return(guesWord)
    
def adaptGuesWord(guesWord):
    new = ""
    for l in guesWord:
        new += l + " "
    return(new)


    



    