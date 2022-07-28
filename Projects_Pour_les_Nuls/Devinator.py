# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import random as rd
import random
import os
import sys


""" Jeu ou le joueur doit deviner le nombre choisi aleatoirement
par l'ordinateur. """


# Regler le pb avec os.system('cls') qui ne fonctionne pas == normal c'est
# os.system('clear')

### Faire evoluer le code avec un niveau de difficulte
### type 0-500, 0-1000
### Envisager un mode reseau avec classement et base de donnees

# Bloc pour demander confirmation pour quitter l'application
QUIT_CONFIRMER = " Voulez-vous vraiment mettre fin a votre partie ? O/n "

# Creation de toutes les variables du code en debut de page.
niveau = 0
rejouer = 1
nbr_secret = 0
nbr_partie = 1
total_tentatives = 0
moyenne_tentatives = 0
compteur_tentatives = 0

########################################################################
################## Debut du programme en dur ###########################
########################################################################

# Entete du jeu. """
print("---------- GAME MAX 2022 ----------\n")
print("Bienvenue sur le DEVINATOR du nombre\n")


# Creation de toutes les fonctions du code en debut de page.

def confirmation_quitter(replay):
    """ Le jeu s'arrete seulement si le joueur saisit 'n'. """
    confi = input(QUIT_CONFIRMER)
    if confi == 'n' or confi =='N' or confi == 'non' or confi == 'Non' or confi == 'NON':
        replay == 1
        return replay
    else :
        replay == 0
        return replay


def jouer_tour():
    """ J'ignore encore a  quoi va servir cette fonction. Elle va
	servir au projet numero 5, Programmer en Python pour les nuls. """

    global niveau
    global rejouer
    global nbr_secret
    global total_tentatives
    global moyenne_tentatives
    global compteur_tentatives
    global nbr_partie

    # Boucle generale debut/fin de jeu.
    while rejouer == 1:

        # Choix de la difficulte
        niveau = 0
        print("CHOIX DE LA DIFFICULTE :")
        print("Niveau 1 - nombre aleatoire entre 0 et 100.")
        print("Niveau 2 - nombre aleatoire entre 0 et 500.")
        print("Niveau 3 - nombre aleatoire entre 0 et 1000.")
        print("Niveau 4 - nombre aleatoire entre 0 et 2000.")

        while niveau != 1 and niveau != 2 and niveau != 3 and niveau != 4:
            niveau = int(input("\nVotre choix : "))

        # Generation du nombre aleatoire.
        if niveau == 1:
            nbr_secret = random.randint(0, 100)
        elif niveau == 2:
            nbr_secret = random.randint(0, 500)
        elif niveau == 3:
            nbr_secret = random.randint(0, 1000)
        else:
            nbr_secret = random.randint(0, 2000)

        os.system('clear')  # Nettoyage de l'affichage de la console.
        print("\nPartie " + str(nbr_partie) + "\n")

        # Bloc pour la saisie du nombre jusqu'a  la reussite.
        while True:

            compteur_tentatives = compteur_tentatives + 1
            nbr_joueur = input("Choisissez un nombre : ")

            if nbr_secret == int(nbr_joueur):
                break
            elif nbr_secret > int(nbr_joueur):
                print('\nPlus grand')
            else:
                print('\nPlus petit')
        print('\nCorrect !')

        # Affichage du nombre de tentatives qui ont ete necessaires pour trouver le nombre secret.
        if compteur_tentatives == 1:
            print("Vous avez reussi en " + str(compteur_tentatives) +
                  " tentative.")
        else:
            print("Vous avez reussi en " + str(compteur_tentatives) +
                  " tentatives.")
        print()

        total_tentatives = total_tentatives + compteur_tentatives

        # Bloc pour demander au joueur de rejouer.
        rejouer = input("Voulez-vous rejouer ? OUI ou NON : ")

        if rejouer == 'OUI' or rejouer == 'oui' or rejouer == 'Oui':
            os.system('cls')  # Nettoyage de l'affichage de la console.
            rejouer = 1
            nbr_partie = nbr_partie + 1
        else:
            confirmation_quitter(rejouer)

# Sortie de la boucle while geneale


# Utilisation de la fonction du cours.
jouer_tour()

# Bloc de fin pour l'affichage des scores.
os.system('cls')  # Nettoyage de l'affichage de la console.
print("\n#########################")
if nbr_partie == 1:
    print("\nVous avez joue 1 partie.")
else:
    print("\nVous avez joue " + str(nbr_partie) + " parties.")

moyenne_tentatives = float(total_tentatives) / nbr_partie


# Bloc pour afficher tentative au singulier ou au pluriel
if moyenne_tentatives == 1:
    print("Moyenne de 1 tentative par partie.")
else:
    print("Moyenne de " + str(moyenne_tentatives) + " tentatives par partie.")
print("\nMerci d'avoir choisi GAME MAX 2022")
print("----------------------------------")
sys.exit()
print(" J'ai baise ta femme. ")
