from random import *

life = int()
myList = []
ghost_word = ""
letter_find = ""


with open('dico_france.txt', 'r') as file:
    myList = file.read().split()
    for i in range(len(myList)):
        myList[i]

random_word = randint(0, len(myList))
good_word = myList[random_word]


for i in range(len(myList[random_word])):
    ghost_word += "_ "


level = str(input("Bonjour à quel niveau souhaites tu jouer (débutant, intermédiaire, expert) ? "))
if level == "débutant":
    life = 10
    print("Nombre de vies : " + str(life))
elif level == "intermédiaire":
    life = 7
    print("Nombre de vies : " + str(life))
elif level == "expert":
    life = 4
    print("Nombre de vies : " + str(life))
else:
    print("Le choix du niveau n'existe pas, veuillez recommencer !")

while life > 0:
    print("Le mot à deviner est : " + ghost_word)
    user_letter = str(input("Veuillez entrer une lettre : "))[0:1].lower()
    if user_letter in good_word:
        letter_find = letter_find + user_letter
    else:
        life = life - 1
        if life == 0:
            print("Vous avez perdu !")
            print("Le mot à trouver été : " + good_word)
            break

    print("Il vous reste " + str(life) + " vies")

    ghost_word = ""
    for x in good_word:
        if x in letter_find:
            ghost_word += x + " "
        else:
            ghost_word += "_ "

    if "_" not in ghost_word:
        print("vous avez gagné !")
        print("Le mot été bien : " + good_word)
        break










