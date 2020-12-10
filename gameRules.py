#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

que fait : fichier qui gere les mechaniques du projet pendu avec interface
qui : FOËX Vick 
quand : 10/12/2020
que reste a faire : 
    
"""

from module import addLettre


def valideLettre(lettre,dico):
    """
    Verifie que le parametre est bien une lettre seul.
    Return1 : la lettre en majuscule 
    Return2 : False si le parametre est incorect
    """

    
    if len(lettre) > 1 or len(lettre) < 1:
        dico["message"] = "lettre invalide"
        return( False )
    
    lettre = lettre.capitalize()
    oLettre = ord(lettre)
    
    if oLettre < ord('A') or oLettre > ord('Z'):
        dico["message"] = "lettre invalide"
        return( False )
    return(lettre)

def askLettre(lettreList, lettre, dico):
    """
    valide la letrre et lance la suite du programme
    """
    lettre = valideLettre(lettre, dico)

    if  lettre != False and usedLettre(lettre, lettreList, dico) == False:
        lettreList.append(lettre)
        checkPresence(lettre, dico)


def  usedLettre(lettre, lettreList, dico):
    if lettre in lettreList :
        dico["message"] = "cette lettre a deja ete choisie"
        return(True)
    return(False)
    
def checkPresence(lettre, dico) :
    """
    Verifie que la lettre est presente dans le mot, la remplace si oui
    sinon stock un message.
    strock ausis le nouveau mot
    """
    word = dico["word"]

    
    if lettre in word :
        for i in range( len( word ) ):
            if word[i] == lettre:
                dico["message"] = "bien jouer !"
                dico["guesWord"] = addLettre(dico["guesWord"], lettre, i)
    else:
        dico["message"] = "la lettre n'est pas dans le mot"
        dico["error"] += 1

    
def genWordUnder(word):
    """
    Genere un str de meme longeur que le parametre avec la premeire lettre 
    visible, les autre sont des _
    """
    
    lenWord = len( word )
    guesWord = word[0] + '_'*(lenWord - 1)
    
    return(guesWord)