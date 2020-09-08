# -*- coding: utf-8 -*-
"""
Author: LaGelee
Description: Mini-projet Lemmings

Date: 07/09/2020
"""

#juste pour pouvoir quitter le programme
import sys

# Classe qui créé les joueurs
class Lemmings(object):
    
    #variables de bases qui définissent le Lemmings à sont arrivée
    def __init__(self, ligne, colonne, direction, j):
        self.ligne = ligne
        self.colonne = colonne
        self.direction = direction
        self.jeu = j
        self.jeu.grotte[self.ligne][self.colonne].arrivee(self)
        
    #return la direction du lemming quand on fait print(Lemming) ----> ">" ou "<"
    def __str__(self):
        return self.direction
    
    #fait déplacer automatiquement le lemming en question sur la nouvelle case (remet bien celle d'avant) ou le fait tourner
    def action(self, index):
        self.index = index
        if self.jeu.grotte[self.ligne+1][self.colonne].libre():
            self.jeu.grotte[self.ligne+1][self.colonne].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].depart()
            self.ligne += 1
        elif self.jeu.grotte[self.ligne][self.colonne-1].libre() and self.direction == "<":
            self.jeu.grotte[self.ligne][self.colonne-1].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].depart()
            self.colonne -= 1
        elif self.jeu.grotte[self.ligne][self.colonne+1].libre() and self.direction == ">":
            self.jeu.grotte[self.ligne][self.colonne+1].arrivee(self)
            self.jeu.grotte[self.ligne][self.colonne].depart()
            self.colonne += 1
        else:
            if self.direction == ">":
                self.direction = "<"
            else:
                self.direction = '>'
    
    #supprimme le lemming de la liste générale et da la partie
    def sort(self):
        self.jeu.grotte[self.ligne][self.colonne].depart() 
        del self.jeu.all[self.index]
          
#Main class initialisation and déroulement
class Jeu(object):
    
    #met en place l'entrée, la map et une liste pour stoquer tous les lemmings (les faire jouer dans l'ordre d'arrivée)
    def __init__(self, grotte, entree):
        self.grotte = grotte
        self.all = []
        self.entree = entree
    
    #affiche la map et les lemmings en faisant print() car chaque caractère est un objet Case
    def affiche(self):
        for elements in self.grotte:
            for car in elements:
                print(car, end='')
            print("")
    
    #fait jouer les lemmings
    def tour(self):
        self.i = 0
        for elements in self.all:
           elements.action(self.i)
           self.i += 1
    
    #fonction princiaple du jeu qui permet de gérer les inputs et faire les actions associées
    def demarre(self):
        while True:
            print("")
            self.affiche()
            cmd = input(">>>")
            if cmd == "l":
                if self.grotte[self.entree[0]][self.entree[1]].libre() :
                    l = Lemmings(self.entree[0],self.entree[1],">",self)
                    self.all.append(l)
                else:
                    print("Attention l'entrée est pleine...")
            elif cmd == 'q':
                break
            else:
                self.tour()   

#Gère toutes les cases et le contenu (lemming,mur,sortie)
class Case(object):
    
    #mets en place les cases avec les caractères "#" et "O" et met lemming à None car pas de lemming de base
    def __init__(self, terrain, lemming):
        self.terrain = terrain
        self.lemming = lemming
    
    #return le caractère de la case ou la direction du lemming si présent
    def __str__(self):
        if self.lemming == None:
            return self.terrain
        else:
            return self.lemming.direction
    
    #return True si case pas occupée par mur ou lemming
    def libre(self):
        if self.terrain != "#" and self.lemming == None:
            return True
    
    #supprime le lemming de la case
    def depart(self):
        self.lemming = None
    
    #fait sortir le lemming si il est sur sortie ou fait associe le lemming à la case
    def arrivee(self, lem):
        if self.terrain == "O":
            lem.sort()
        else:
            self.lemming = lem
    
    
#récupère la map et la met dans un tableau avec des instances Case pour chaque
def map(fichier):
    files = open(fichier, "r")
    tableau = []

    for ligne in files:
        line = []
        for car in ligne.strip('\n'):
            case = Case(car, None)
            line.append(case)
        tableau.append(line)
    files.close()

    return tableau

#rècupère le tableau de la map
fichier = "carte.txt"
tableau = map(fichier)

#met en place le jeu et le lance 
game = Jeu(tableau,[0,1])
game.demarre()

#petit affichage de fin
print()
print("Finish...")
input()
