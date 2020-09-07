# -*- coding: utf-8 -*-
"""
Author: LaGelee
Description: Mini-projet Lemmings

Date: 07/09/2020
"""

import sys

# Classe qui créé les joueurs
class Lemmings(object):
    
    def __init__(self, ligne, colonne, direction, j):
        self.ligne = ligne
        self.colonne = colonne
        self.direction = direction
        self.jeu = j
        self.jeu.grotte[self.ligne][self.colonne].arrivee(self)
        
    def __str__(self):
        return self.direction
    
    def action(self, index):
        self.index = index
        if self.jeu.grotte[self.ligne+1][self.colonne].libre():
            self.jeu.grotte[self.ligne+1][self.colonne].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].terrain = " "
            self.jeu.grotte[self.ligne][self.colonne].lemming = None
            self.ligne += 1
        elif self.jeu.grotte[self.ligne][self.colonne-1].libre() and self.direction == "<":
            self.jeu.grotte[self.ligne][self.colonne-1].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].terrain = " "
            self.jeu.grotte[self.ligne][self.colonne].lemming = None
            self.colonne -= 1
        elif self.jeu.grotte[self.ligne][self.colonne+1].libre() and self.direction == ">":
            self.jeu.grotte[self.ligne][self.colonne+1].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].terrain = " "
            self.jeu.grotte[self.ligne][self.colonne].lemming = None
            self.colonne += 1
        else:
            if self.direction == ">":
                self.direction = "<"
            else:
                self.direction = '>'
            
    def sort(self):
        self.jeu.grotte[self.ligne][self.colonne].terrain = "O"
        self.jeu.grotte[self.ligne][self.colonne].lemming = None    
        del self.jeu.all[self.index]
          
#Main class initialisation and déroulement
class Jeu(object):
    
    def __init__(self, grotte):
        self.grotte = grotte
        self.all = []
    
    def affiche(self):
        for elements in self.grotte:
            for car in elements:
                print(car, end='')
            print("")
    
    def tour(self):
        self.i = 0
        for elements in self.all:
           elements.action(self.i)
           self.i += 1
    
    def demarre(self):
        while True:
            print("")
            self.affiche()
            cmd = input(">>>")
            if cmd == "l":
                l = Lemmings(0,1,">",self)
                self.all.append(l)
            elif cmd == 'q':
                sys.exit(1)
            else:
                self.tour()   

    
class Case(object):
    
    def __init__(self, terrain, lemming):
        self.terrain = terrain
        self.lemming = lemming
    
    def __str__(self):
        if self.lemming == None:
            return self.terrain
        else:
            return self.lemming.direction
    
    def libre(self):
        if self.terrain != "#" and self.lemming == None:
            return True
    
    def depart(self):
        self.lemming = None
    
    def arrivee(self, lem):
        if self.terrain == "O":
            lem.sort()
        else:
            self.lemming = lem
    
    
#démarrage du jeu
file = "carte.txt"

fichier = open(file, "r")

tableau = []

for ligne in fichier:
    line = []
    for car in ligne.strip('\n'):
        case = Case(car, None)
        line.append(case)
    tableau.append(line)
fichier.close()

game = Jeu(tableau)
game.demarre()

print()
print("Finish...")
