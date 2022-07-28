# -*- coding: utf-8 -*-

""" Cryptage et decryptage de chaines avec la methode Cesar. """

# Imports
import string

# CONSTANTES
JEUCAR = string.printable[:-5]
CARSUBSTIT = JEUCAR[-3:] + JEUCAR[:-3]
MSG_TEST = "J'adore les Monty Python. Trop cool."

DICO_ENCRYP = {} # Creation et assignation du dictionnaire avec les 2 listes.
DICO_DECRYP = {} # Dictionnaire de decryptage
for i, k in enumerate(JEUCAR):
    v = CARSUBSTIT[i]
    DICO_ENCRYP[k] = v
    DICO_DECRYP[v] = k
for c in string.printable[-5:]:
    DICO_ENCRYP[c] = c
    DICO_DECRYP[c] = c


# Fonction
def encrypter(texteclair, vardico_cryp):
    """ Crypte le texteclair avec la methode de chiffrement Cesar. """
    textesecret = []
    for k in texteclair:
        v = vardico_cryp[k]
        textesecret.append(v)
    return ''.join(textesecret) # Pas de traitement pour le moment.

def decrypter(textesecret, vardico_decryp):
    """ Decrypte le textesecret chiffre en Cesar. """
    texteclair = []
    for k in textesecret:
        v = vardico_decryp[k]
        texteclair.append(v)
    return ''.join(texteclair) # Pas de traitement pour le moment.


# Fonction MAIN
print("* * * Projet Cryptopy v4.0 * * *")
texte_a_traduire = (input("Texte à crypter : \n"))
textesecret = encrypter(texte_a_traduire, DICO_ENCRYP)
texteclair = decrypter(textesecret, DICO_DECRYP)
print("Texte crypte : \n\n" + str(textesecret))
print("\n")
print("Texte decrypter : \n\n" + str(texteclair))
print("\n")
print("Est-ce que le texte initial et le texte decrypte sont les meme ? : "
+ str(texte_a_traduire == texteclair))
