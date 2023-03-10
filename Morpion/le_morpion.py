myList = []
joueur_1 = "X"
joueur_2 = "O"

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

i = 0
while i < 9:
    current_player = joueur_1 if i % 2 == 0 else joueur_2
    choice = int(input("Joueur " + current_player + " choisit un nombre : "))
    current_choice = choice if current_player == joueur_1 else current_player == joueur_2

    if choice == 1:
        if affichage[0] == "_":
            affichage[0] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 2:
        if affichage[1] == "_":
            affichage[1] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 3:
        if affichage[2] == "_":
            affichage[2] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 4:
        if affichage[4] == "_":
            affichage[4] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 5:
        if affichage[5] == "_":
            affichage[5] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 6:
        if affichage[6] == "_":
            affichage[6] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 7:
        if affichage[8] == "_":
            affichage[8] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 8:
        if affichage[9] == "_":
            affichage[9] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice == 9:
        if affichage[10] == "_":
            affichage[10] = current_player
        else:
            print("Ce choix de case a déjà été pris !")
            i += -1
    elif choice >= 10 or choice <= 0:
        print("Veuillez choisir une valeur entre 1 et 9 !")
        i += -1


    game = "{} {} {} \n".format(affichage[0], affichage[1], affichage[2])
    game += "{} {} {} \n".format(affichage[4], affichage[5], affichage[6])
    game += "{} {} {}".format(affichage[8], affichage[9], affichage[10])

    print(game)

    if affichage[0] == affichage[1] == affichage[2]:
        if affichage[0] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[4] == affichage[5] == affichage[6]:
        if affichage[4] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[8] == affichage[9] == affichage[10]:
        if affichage[8] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[0] == affichage[4] == affichage[8]:
        if affichage[0] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[1] == affichage[5] == affichage[9]:
        if affichage[1] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[2] == affichage[6] == affichage[10]:
        if affichage[2] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[0] == affichage[5] == affichage[10]:
        if affichage[0] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif affichage[2] == affichage[5] == affichage[10]:
        if affichage[2] == current_player:
            print("Joueur " + current_player + " à gagné !")
            break
    elif i == 8:
        print("Egalité !")
    i += 1
