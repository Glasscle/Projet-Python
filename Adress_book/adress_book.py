"""
carnet.py
Logiciel de gestion d'un carnet d'adresse avec prenom, nom, date de naissance
et courriel.
Cree par Ccixon S.
"""

### Section des imports
import pickle
import os.path

### Section des classes
class CarnetAdr(object):
    """ Carnet de fiches. """
    def __init__(self):
        """ Initialisation du carnet de fiches. """
        self.gens = []

    def ajouter_fiche(self, fiche_nouvo):
        """ Ajouter la fiche 'fiche_nouvo' dans le carnet d'adresse. """
        self.gens.append(fiche_nouvo)

    def sauver(self):
        """ Sauvegarder le carnet dans un fichier pickle. """
        with open(NOMFIC_SAUVE, "wb") as ficow:
            pickle.dump(self, ficow)


class FicheAdr(object):
    """ Fiche d'un contact """
    def __init__(self, prenom = None, nomfami = None, datenaiss = None, courriel = None):
        """ Initialisation des 4 attributs de la classe.
        La date de naissance doit se formater JJ/MM/AAA. """
        self.prenom = prenom
        self.nomfami = nomfami
        self.datenaiss = datenaiss
        self.courriel = courriel

    def __repr__(self):
        """ Afficher le contenu de la classe FicheAdr. """
        patron = "FicheAdr(prenom = '%s', nomfami = '%s', datenaiss = '%s', courriel = '%s')"
        patron = patron % (self.prenom, self.nomfami, self.datenaiss, self.courriel)
        return patron


class Kontroleur(object):
    """ Pour gerer les donnees stockees dans une instance de CarnetAdr, le menu et
    le chargement des donnees du fichier.
    METHODES : __init__, charger()"""

    def __init__(self):
        """ Cherche un fichier. S'il le trouve, il le lit. Sinon, il cree un fichier vide. """
        self.carnet_adr = self.charger()
        if self.carnet_adr is None:
            self.carnet_adr = CarnetAdr()
        self.gerer_menu()

    def charger(self):
        """ Charge un carnet depuis un fichier pickle. """
        if os.path.exists(NOMFIC_SAUVE):
            with open(NOMFIC_SAUVE, "rb") as ficor:
                return pickle.load(ficor)
        else:
            return None

    def gerer_menu(self):
        """ Gerer le menu pour le choix de l'utilisateur. Boucle centrale de
        l'application. Obtient la commande clavier et lance l'action. """
        print(INSTRUCTIONS)
        while True:
            cmd = input("\nVotre choix ? : ")
            if cmd == "a" or cmd == "A":
                self.ajouter_fiche()
            elif cmd == "q" or cmd == "Q":
                if confirmer_quitter():
                    print("Sauvegarde")
                    self.carnet_adr.sauver()
                    print("Fin de l'application.")
                    break
            elif cmd == "i" or cmd == "I":
                print(INSTRUCTIONS)
            elif cmd == "l" or cmd == "L":
                self.lister_fiches()
            else:
                modele = "*** Touche de commande inconnue (%s) !"
                print(modele%cmd)

    def ajouter_fiche(self):
        """ Demande la saisie des champs de la nouvelle liste. """
        nom = input("\nNom : ")
        if nom == "q":
            print("Abandon de la creation.")
            return
        prenom = input("Prenom : ")
        if prenom == "q":
            print("Abandon de la creation.")
            return
        datenaiss = input("Date de naissance au format JJ/MM/AAAA : ")
        if datenaiss == "q":
            print("Abandon de la creation.")
            return
        courriel = input("Courriel : ")
        if courriel == "q":
            print("Abandon de la creation.")
            return
        nfiche = FicheAdr(prenom, nom, datenaiss, courriel)
        self.carnet_adr.ajouter_fiche(nfiche)

    def lister_fiches(self):
        """ Afficher la liste des contacts du carnet d'adresse. """
        print("")
        for indice, i in enumerate(self.carnet_adr.gens):
            contact = (i.prenom, i.nomfami, i.datenaiss, i.courriel)
            patron = "%s %s - Date de naissance : %s - courriel : %s"
            print((str(indice + 1) + " : " + patron%contact))



### Section des CONSTANTES et variables
NOMFIC_SAUVE = "carnet.pickle"
QUIT_CONFIRMER = "Vous confirmez vouloir quitter ? (O/N) "
INSTRUCTIONS = """ *********************************************
Application Carnet d’Adresses
(Python en s’amusant Pour les Nuls, Projet 9)
*********************************************
Tapez une des quatre touches suivantes :
A pour Ajouter une personne
L pour la Liste des fiches du carnet
I pour revoir ces Instructions
Q pour Quitter. """
PATRON_LISTE = "%s %s - Naissance : %s - Email %s"

### Section des fonctions
def confirmer_quitter():
    """ On sort seulement si saisie de la lettre minuscule n par renvoi de
    False. """
    confi = input(QUIT_CONFIRMER)
    if confi == 'n' or confi =="N":
        return False
    else:
        return True

### Section MAIN
if __name__ == "__main__":
    controleur = Kontroleur() # Creation classe controleur
    # print(controleur.carnet_adr.gens) # Impression classe controleur
