#-------------------------------------------------------------------------------
# Name:        phrazenfolie.py
# Purpose:      Generer des phrases bizarres aleatoires en utilisant des
#               Patrons de chaines.
#
# Author:      Julien S.
#
# Created:     12/04/2022
# Copyright:   (c) Julien S. 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Section import
import random

# Section CONSTANTES et variables
PHRASE_BASE = "Mon professeur programme un jeu formidable."

patron = "%s %s %s %s." # Structure de nos phrases "sujet verbe objet qualificatif)

sujets = ["Mon professeur" ,"Ma guitare" ,"Le travail" , "le conge", "La voiture", "Le magasin" , "Le directeur", "La banquiere", "Le puiguin" ,"Le bigorneau" ,"La stripteaseuse" ,"La courtisane" ,"Le garagiste" ,"Le demarcheur" ,"Le surfeur" ,"Trump" , "Le canibal", "Le tueur a gage"] # Variables qui contiennent les listes de type de mots de nos phrases.
verbes = ["programme" ,"achete" ,"mange" ,"choisit" ,"prend" , "depoussiere" ,"calcule" ,"brule", "est", "possede" ,"harcele", "facture", "puni", "cache", "sodomise", "raquette", "falsifie", "demonte", "cree", "nie", "impose","corrige","broie","reverse","doigte","penetre"]
objets = ["un jeu" ,"la voisine" ,"l'arbre" ,"le cimetiere" ,"un verre de vin" ,"une sucette" ,"l'election presidentielle" ,"le lit", "le salsifi", "le paquet de cereal", "le gode", "l'ordinateur","le rat","la chicha","l'abruti du village","le whisky","le pestifere","le melon","l'impot sur le revenu","le temoin de Jeova","l'huitre","la maitresse","le boucher","le cordonnier","le flic"]
kalifs = ["formidable" ,"diurne" ,"pourri" ,"lamentable" ,"rebarbatif" ,"juxtapose" ,"inadvertant" ,"magnifique" ,"incontinant" ,"nevrose" ,"schizophrene" ,"paranoiaque" ,"heureux" ,"bon vivant" , "radin econome" ,"nymphomane" ,"chien de la casse" ,"hyperactif" ,"colabo" ,"accro au jeu" ,"pantouflard" ,"rageur" ,"moldu" ,"obese" ,"frigide" ,"emotif", "anorexique", "crade", "monocouille"]



# Section fonctions

def creation_phrase(patron, sujets, verbes, objets, kalifs, PHRASE_BASE):
    """ Assemblage d'une phrase avec les 4 types de mots en argument. """
    correspondance = (patron % (sujets, verbes, objets, kalifs) == PHRASE_BASE)
    return correspondance



# Section MAIN

if __name__ == "__main__" : # Pour que seules les fonctions soient reutilises par d'autres fichiers.
    compteur = 0
    while compteur < 11:
        compteur = compteur + 1
        sujet = random.choice(sujets)
        verbe = random.choice(verbes)
        objet = random.choice(objets)
        kalif = random.choice(kalifs)

        valformat = (sujet, verbe, objet, kalif)
        print(patron % valformat)
##        print(PHRASE_BASE == (patron % valformat))
##        print(creation_phrase(patron, sujet, verbe, objet, kalif, PHRASE_BASE))


"""
Le tueur a gage achete le gode bon vivant.
La voiture sodomise le melon inadvertant.
le conge choisit le melon colabo.
Le canibal harcele la chicha schizophrene.
Le bigorneau choisit une sucette colabo.
La courtisane falsifie l'abruti du village monocouille.
Le travail est une sucette colabo.
Le canibal brule le temoin de Jeova hyperactif.n/c

"""
