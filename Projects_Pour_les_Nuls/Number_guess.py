# -*- coding: utf-8 -*-

""" Projet 5 JeuDevin.py Version 4 (finale) """

import random

INVITE = 'Propose un nombre : '

# Nouvelles constantes
QUITTER = -1
QUIT_TXT = 'q'
QUIT_MSG = 'Merci pour tout !'
QUIT_CONFIRMER = "Es-tu certain de vouloir quitter (o/n) ? : "


# Nouvelle fonction pour confirmer qu'on veut quitter
def confirmer_quitter():
    """ On sort seulement si saisie de la lettre minuscule n par renvoi de
    False. """
    confi = input(QUIT_CONFIRMER)
    if confi == 'n' or confi =="N":
        return False
    else:
        return True

def jouer_tour():
    """ Choisir un nombre, demander au joueur de le trouver et de reboucler
    tant qu'il ne l'a pas. """
    nbr_secret = random.randint(1, 100)
    nbr_saisies = 0
# Ajout
    while True:
        nbr_joueur = input(INVITE)
        # Ajout bloc if pour sortie confirmee
        if nbr_joueur == QUIT_TXT:
            if confirmer_quitter():
                return QUITTER
            else:
                continue # Tour de boucle suivant
        nbr_saisies = nbr_saisies + 1
        if nbr_secret == int(nbr_joueur):
            print('Correct !')
            return nbr_saisies
        elif nbr_secret > int(nbr_joueur):
            print('Trop petit')
        else:
            print('Trop grand')


# Section principale MAIN
total_tours = 0
total_saisies = 0
msg_stat = 0

while True:
    total_tours = total_tours + 1
    print("")
    print("On passe au tour " + str(total_tours))
    print("En avant pour les devinettes !")

    ce_tour = jouer_tour()

    # Ajout du bloc if pour tester si quitter
    if ce_tour == QUITTER:
        total_tours = total_tours - 1
        if total_tours == 0:
            msg_stat = "1er tour pas fini ! \n" + "Tu veux recommencer ?"
        else :
            moy = str(total_saisies / float(total_tours))
            msg_stat = "Tu as fait " + str(total_tours) + " tours. Moyenne de " + str(moy)
            break
    else:
        total_saisies = total_saisies + ce_tour

print("Tu as fait " + str(total_saisies) + " saisies.")
moy = str(total_saisies / float(total_tours))
print("Ta moyenne est de " + str(moy))
print("")

# Message de sortie
print(QUIT_MSG)
print(msg_stat)
