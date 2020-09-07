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
        
    def __str__(self):
        return self.direction
    
    def action(self):
        if self.jeu.grotte[self.ligne+1][self.colonne].libre():
            self.jeu.grotte[self.ligne+1][self.colonne].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].terrain = " "
            self.ligne += 1
        elif self.jeu.grotte[self.ligne][self.colonne-1].libre() and self.direction == "<":
            self.jeu.grotte[self.ligne][self.colonne-1].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].terrain = " "
            self.colonne -= 1
        elif self.jeu.grotte[self.ligne][self.colonne+1].libre() and self.direction == ">":
            self.jeu.grotte[self.ligne][self.colonne+1].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].terrain = " "
            self.colonne += 1
        else:
            if self.direction == ">":
                self.direction = "<"
            else:
                self.direction = '>'
            
            
    def sort(self):
        self.jeu.grotte[self.ligne][self.colonne].terrain = "O"
        self.jeu.grotte[self.ligne][self.colonne].lemming = None
        
        
    
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
        for lim in self.all:
            lim.action()
        self.affiche()
    
    def demarre(self):
        try: 
            while True:
                cmd = input(">>>")
                if cmd == "l":
                    l = Lemmings(0,1,">",self)
                    self.all.append(l)
                elif cmd == 'q':
                    sys.exit(1)
                else:
                    self.tour()
                    
                self.affiche()
                
        except Exception as e:
            print(e)
            sys.exit(1)
    
class Case(object):
    
    def __init__(self, terrain, lemming):
        self.terrain = terrain
        self.lemming = lemming
    
    def __str__(self):
        if self.lemming == None:
            return self.terrain
        else:
            return self.lemming
    
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
try:
    file = "lemmings-carte.txt"
    
    fichier = open(file, "r")
    
    tableau = []
    
    for ligne in fichier:
        line = []
        for car in ligne.strip('\n'):
            case = Case(car, None)
            line.append(case)
        tableau.append(line)
    fichier.close()
    
    print(tableau)
    print("ok")
    
    game = Jeu(tableau)
    game.demarre()
except Exception as e:
    print("Erreur avec le fichier...")
    print(e)
finally:
    print()
    print("Finish...")
