
# import random
#
# prix = random.randint(1,10)
#
#
# rep = input("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")
# while intrep != prix :
#     intrep = int(rep)
#     tent = 1
#
#     if intrep == prix :
#         print("Félicitations, vous avez trouvé le juste prix", prix, "en", tent, "essais, votre score est !")
#         print("Partie terminée")
#
#     while rep != prix :
#
#         if intrep > 10:
#             print("Veuillez saisir un chiffre compris entre 1 et 10 inclus")
#             tent = tent + 1
#             break
#
#         if intrep < prix:
#             print("Le juste prix est plus haut")
#             tent = tent + 1
#             break
#         if intrep > prix:
#             print("Le juste prix est plus bas")
#             tent = tent + 1
#             break

#print(prix)
#print(rep)

import random

prix = random.randint(1, 10)

score = 100

tentatives = 0

#print("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus.")

while True:
    nombre = int(input("Devinez le juste prix ! Le prix est un nombre compris entre 1 et 10 inclus."))
    tentatives += 1

    if nombre < prix:
        print("Le just prix est plus haut")
    if nombre > prix:
        print("Le juste prix est plus bas")
    if nombre == prix:
        print("Félicitations, vous avez trouvé le juste prix {} en {} essais, votre score est {} !".format(prix, tentatives, int(score / tentatives)))
        break

score = score/tentatives
print("Partie terminée")
print(score)