
myList = []

for i in range(3):
    for x in range(3):
        myList.append("_")

affichage = []
for i in range(3):
    for x in range(3):
        affichage += myList[i]
    affichage += "\n"


game = "{} {} {} \n".format(affichage[0], affichage[1], affichage[2])
game += "{} {} {} \n".format(affichage[4], affichage[5], affichage[6])
game += "{} {} {}".format(affichage[8], affichage[9], affichage[10])

print(game)

joueur_1 = "X"
joueur_2 = "O"
i = 0
while i < 9:
    if i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
        choice_j1 = int(input("joueur " + joueur_1 + " choisit un nombre : "))
        if choice_j1 == 1:
            if affichage[0] == "_":
                affichage[0] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 2:
            if affichage[1] == "_":
                affichage[1] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 3:
            if affichage[2] == "_":
                affichage[2] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 4:
            if affichage[4] == "_":
                affichage[4] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 5:
            if affichage[5] == "_":
                affichage[5] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 6:
            if affichage[6] == "_":
                affichage[6] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 7:
            if affichage[8] == "_":
                affichage[8] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 8:
            if affichage[9] == "_":
                affichage[9] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 == 9:
            if affichage[10] == "_":
                affichage[10] = joueur_1
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j1 >= 10:
            print("Veuillez choisir une valeur entre 1 et 9 !")
            i += -1
    elif i == 1 or i == 3 or i == 5 or i == 7:
        choice_j2 = int(input("joueur " + joueur_2 + " choisit un nombre : "))
        if choice_j2 == 1:
            if affichage[0] == "_":
                affichage[0] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 2:
            if affichage[1] == "_":
                affichage[1] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 3:
            if affichage[2] == "_":
                affichage[2] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 4:
            if affichage[4] == "_":
                affichage[4] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 5:
            if affichage[5] == "_":
                affichage[5] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 6:
            if affichage[6] == "_":
                affichage[6] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 7:
            if affichage[8] == "_":
                affichage[8] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 8:
            if affichage[9] == "_":
                affichage[9] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 == 9:
            if affichage[10] == "_":
                affichage[10] = joueur_2
            else:
                print("Ce choix de case a déjà été pris !")
                i += -1
        elif choice_j2 >= 10:
            print("Veuillez choisir une valeur entre 1 et 9 !")
            i += -1

    game = "{} {} {} \n".format(affichage[0], affichage[1], affichage[2])
    game += "{} {} {} \n".format(affichage[4], affichage[5], affichage[6])
    game += "{} {} {}".format(affichage[8], affichage[9], affichage[10])

    print(game)

    if affichage[0] == affichage[1] == affichage[2]:
        if affichage[0] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[0] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[4] == affichage[5] == affichage[6]:
        if affichage[4] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[4] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[8] == affichage[9] == affichage[10]:
        if affichage[8] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[8] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[0] == affichage[4] == affichage[8]:
        if affichage[0] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[0] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[1] == affichage[5] == affichage[9]:
        if affichage[1] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[1] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[2] == affichage[6] == affichage[10]:
        if affichage[2] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[2] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[0] == affichage[5] == affichage[10]:
        if affichage[0] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[0] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif affichage[2] == affichage[5] == affichage[10]:
        if affichage[2] == "X":
            print("Joueur " + joueur_1 + " à gagné !")
            break
        elif affichage[2] == "O":
            print("Joueur " + joueur_2 + " à gagné !")
            break
    elif i == 8:
        print("Egalité !")
    i += 1
























