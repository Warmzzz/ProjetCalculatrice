
while True:
    try:
        choix = int(input("©Copyright 2021 Gigantelli Raffaele - Tous droits réservés\n\n1)Addition\n2)Soustraction\n3)Multiplication\n4)Division\n\nChoisissez une opération : "))
        break
    except ValueError:
        print("!!! Choisissez un des 4 chiffres pour effectuer une opération !!!\n")
        continue

def addition():
    if choix == 1:
        while True:
            try:
                addition1 = int(input("Entrez le premier nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        while True:
            try:
                addition2 = int(input("Entrez un deuxième nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !")
                continue

        calcul1 = int(addition1) + int(addition2)
        print("Le résultat de l'addition de ", addition1, "avec ", addition2, "est égal à", calcul1)

def soustraction():
    if choix == 2:
        while True:
            try:
                soustraction1 = int(input("Entrez le premier nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        while True:
            try:
                soustraction2 = int(input("Entrez un deuxième nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        calcul2 = int(soustraction1) - int(soustraction2)
        print("Le résultat de la soustraction entre", soustraction1, "entre", soustraction2, "est égal à", calcul2)

def multiplication():
    if choix == 3:
        while True:
            try:
                multiplication1 = int(input("Entrez le premier nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        while True:
            try:
                multiplication2 = int(input("Entrez un deuxième nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        calcul3 = int(multiplication1) * int(multiplication2)
        print("Le résultat de la multiplication de", multiplication1, "par", multiplication2, "est égal à", calcul3)

def division():
    if choix == 4:
        while True:
            try:
                division1 = int(input("Entrez le premier nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        while True:
            try:
                division2 = int(input("Entrez un deuxième nombre :"))
                break
            except ValueError:
                print("Veuillez entrer un nombre !\n")
                continue

        calcul4 = int(division1) / int(division2)
        print("Le résultat de la division de", division1, "par", division2, "est égal à", calcul4)

if choix == 1:
    addition()
if choix == 2:
    soustraction()
if choix == 3:
    multiplication()
if choix == 4:
    division()