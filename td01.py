###programationTD1###

#exercice1#

#we generate a random list of letters (tirage) then we split all the words from the dictionary into a list of letters to compare the letters of the words and the letters of tirage. We then store the words containing at least one draw letter in a list. We remove the words from this list containing other letters than the one from tirage and we keep the longest words


#Exercice 2

import numpy as np
from os import chdir
import random
# opening the dictionary that we will use later
dico = [] #list of all the words
f = open('mots.sansaccent.txt','r')
# dictionary sort
for ligne in f :
         dico.append(ligne[0:len(ligne)-1])
f.close()
def scrable(n,dico):

    # I'm creating the list of letters we want to work with
    mots_possibles= []
    tirage= [] # letters we want to create words with
    alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while len(tirage)<n:
        lettre=alphabet[random.randrange(1,26,1)]
        if lettre in tirage:
            None
        else:
            tirage.append(lettre)

    # I'm looking for the longuest word we can create with the letters in tirage that is in dico

    for element in dico:
        element_split=list(element) # we split the word
        for lettre in tirage:
            if lettre in element_split and element_split not in mots_possibles: # we create the list in which we have all the words with at least one letter of tirage in
                mots_possibles.append(element_split)

    for mot in mots_possibles:
        if lettre in mot not in tirage: # we take out all the words that also have other letters than the ones that are in tirage
            mots_possibles.pop(mot)

    return max([(len(element),element) for element in mots_possibles])



#Exercice 3

#the structure we need to associate a number of points to a draw is a dictionary

#Question 3 : The structure we're looking to use is that of a dictionary, because we need to link each letter to its set score

scores = dict([(lettre,1) for lettre in ['a','e','i','l','n','o','r','s','t','u']]+[(lettre,2) for lettre in ['d','g','m']]+[(lettre,3) for lettre in ['b','c','p']]+[(lettre,4) for lettre in ['f','h','v']]+[(lettre,8) for lettre in ['j','q']]+[(lettre,10) for lettre in ['k','w','x','y','z']])

def score(mot):
    s=0
    mot_split=list(mot)
    for lettre in mot_split:
        s+=scores[str(lettre)]
    return s

def max_score(liste_mot):
    return max([(score(element),element) for element in liste_mot])

def scrablemax(n,dico):
    mots_possibles= []
    tirage= [] # letters we want to create words with
    alphabet= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    while len(tirage)<n:
        lettre=alphabet[random.randrange(1,26,1)]
        if lettre in tirage:
            None
        else:
            tirage.append(lettre)

    # I'm looking for the longuest word we can create with the letters in tirage that is in dico

    for element in dico:
        element_split=list(element) # we split the word
        for lettre in tirage:
            if lettre in element_split:# we create the list in which we have all the words with at least one letter of tirage in
                mots_possibles.append(element_split)

    for mot in mots_possibles:
        compteur=0
        for lettre in mot: # we take out all the words that also have other letters than the ones that are in tirage
            if lettre not in tirage:
                compteur+=1
        if compteur>0:
            mots_possibles.remove(mot)

    return max([(len(element),element) for element in mots_possibles])

