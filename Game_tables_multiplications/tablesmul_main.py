# -*- coding: utf-8 -*-

"""
Projet 10 - Programmer en Python pour les nuls

Jeu qui demande a l'utilisateur de repondre a des questions sur les tables de
multiplications, avec compteur de score et chronometre.

Cree par Ccixon S.
"""

""" RESTE A FAIRE
- Creer un Menu.
- Creer le texte pour "quitter en tappant Q".
- Trouver le moyen de creer une base de donnee/fichier pour stocker les resultats,
les charger ainsi que de les trier en fonction du meilleur score.
"""

### Rendre les scores equitables.

### Section import ###########################################################
from datetime import date
import random
import sys
import time
import pandas as pandasForSortingCSV
import csv
import os.path

### Section CONSTANTES #######################################################
FIELDS = ['Date', 'namePlayer', 'Score', 'Time']
SAVE_CSV_FILE = "tablesmul_scores.csv"
QUESTION_PATTERN = "Combien font %s et %s ? : "
FIRST_TABLE_NUMBER = 1
LAST_TABLE_NUMBER = 12
QUESTIONS_MAX_PER_GAME = 20
DISPLAY_TABLE_ROW = "%2i x %2i = %3i    "
APP_HEADER = """-------------------------------------
REVISE TES TABLES DE MULTIPLICATIONS
et DEFIE TES AMIS !
Tables de 1 à 12
-------------------------------------"""
FIN = """ Cree par Ccixon """
MENU = """\n-------------- MENU -----------------\n
1 - Reviser les tables de 1 a 12
2 - Commencer une partie
3 - Afficher les scores
4 - Quitter
Votre choix : """
PATRON_PRINT_SCORE = "Ton score est de %s (%i%%) en %.1f secondes.\n"
QUIT_CONFIRM = "Es-tu certain de vouloir quitter (o/n) ? : "


### Section fonctions #########################################################
def checkExistsCsvFile(SAVE_CSV_FILE):
    """ Check the existance of the csv file. """
    if os.path.exists(SAVE_CSV_FILE) == False: # Si le fichier existe déja, le lire
            with open(SAVE_CSV_FILE, 'w') as createCsvFile:
                csvwriter = csv.writer(createCsvFile)
                csvwriter.writerow(FIELDS)

def readLinesCsvFile(fichierCsv):
    """ Lire le contenu du fichierCsv ligne par ligne. """
    with open(SAVE_CSV_FILE, 'r') as csvfile_r:
        csv.reader(csvfile_r)
        for row in csvfile_r:
            print(row)
    print("Fin de la lecture du fichier csv.") # TEST, a enlever

def generateListQuestions(nmin = FIRST_TABLE_NUMBER, nmax = LAST_TABLE_NUMBER, hasard = True):
    """ Cree une liste de questions au format (x, y) avec x et y compris entre
    1 et 12. Si hasard = True, la liste est generee au hasard. Si False, non. """
    tempo = [(x+1, y+1) for x in range(nmin-1, nmax) for y in range(nmin-1, nmax)]
    if hasard:
        random.shuffle(tempo)
    return tempo

def startGame():
    """ Tester. """
    print("\n")
    namePlayer = ""
    while namePlayer == "":
        namePlayer = input("Saisiez votre pseudo : ")
    liste_q = generateListQuestions()
    rightAnswer = 0
    timeStartGame = time.time() # L'heure du debut du test
    for i, question in enumerate(liste_q):
        if i >= QUESTIONS_MAX_PER_GAME:
            break
        invite = QUESTION_PATTERN % question
        reponse_ok = question[0]*question[1]
        saisie = ""
        while saisie.isdigit() == False:
            saisie = input(invite)
        if int(saisie) == reponse_ok:
            print("Correct !")
            rightAnswer += 1
        else :
            print("Incorrect, c'etait %s."%(reponse_ok))
    gameTime = round((time.time() - timeStartGame), 1)
    gameScore = round((rightAnswer / QUESTIONS_MAX_PER_GAME * 100))
    todayDate = date.today()
    print("\nNombre de calculs corrects : %s"%rightAnswer)
    print(PATRON_PRINT_SCORE%(rightAnswer, gameScore, gameTime))
    addNewEntry(SAVE_CSV_FILE, todayDate, namePlayer, gameScore, gameTime)

def displayTables(nmax = LAST_TABLE_NUMBER):
    """ Afficher les tables de multiplications. """
    print("\n")
    tab_par_lig = 4
    tab_total = range(1, LAST_TABLE_NUMBER + 1) # Soit ici 12.
    lot_tab = tab_total[:tab_par_lig] # Prends un lot de 5 pour l'affichage.
    tab_total = tab_total[tab_par_lig:] # Les enleve du stock restant.
    while lot_tab != range(13, 13): # Stop quand vide.
        for x in range(1, LAST_TABLE_NUMBER + 1): # traîter les nombres de 1 à 12.
            accumul = [] # Stock 1 ligne d'une table.
            for y in lot_tab: # Construit les colonnes.
                accumul.append(DISPLAY_TABLE_ROW%(y, x, x * y)) # Stock une ligne dans accumul[]
            print("".join(accumul)) # Affiche la ligne créée avec y
        print("\n") # Separation verticale entre blocs de tables.
        lot_tab = tab_total[:tab_par_lig] # Prends un lot de 5 pour l'affichage.
        tab_total = tab_total[tab_par_lig:]

def addNewEntry(fichierCsv, todayDate, namePlayer, gameScore, gameTime):
    """ Add a new entry to the existing csv file. """
    with open(SAVE_CSV_FILE, 'a+') as fichierCsv:
        csvwriter = csv.writer(fichierCsv)
        csvwriter.writerow([todayDate, namePlayer, gameScore, gameTime])
    print("Les donnees de la partie ont ete ajoute avec succes.")

def displayScores(fichierCsv):
    """ Displaying scores from SAVE_CSV_FILE sorted by 'Score' and 'Time' fields. """
    csvData = pandasForSortingCSV.read_csv(fichierCsv)
    csvData.columns = csvData.columns.str.strip() # Clean the space before and after.
    csvData = csvData.sort_values(['Score', 'Time'], ascending = [False, False])
    print("\n\n------------ CLASSEMENT -------------\n")
    print(csvData)
    print("\n")

def quitApp():
    """ Demander a l'utilisateur de confirmer l'arret du programme. """
    if confirmQuitApp() :
        sys.exit()
    print("Dans quitter() mais on fait demi-tour.")

def confirmQuitApp():
    """ On sort de la fonction seulement si saisie de la lettre minuscule n par
    renvoi de False. """
    confi = input(QUIT_CONFIRM)
    if confi == 'n' or confi =="N":
        return False
    else:
        return True

### Section MAIN ############################################################
if __name__ == "__main__":
    print(APP_HEADER)
    checkExistsCsvFile(SAVE_CSV_FILE)
    while True:
        selection = input(MENU) # Affichage du menu
        selection = selection.strip() # Cut les espaces avant et après la saisie.
        if selection == '1':
            displayTables() # Revision tables de multiplications
        elif selection == '2':
            startGame()
        elif selection == '3':
            displayScores(SAVE_CSV_FILE)
        elif selection == '4':
            quitApp()
        else:
            print("Saisie invalide. Votre choix : ")
