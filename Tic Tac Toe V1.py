# Het idee is om een boter-kaas-en-eieren spel te maken dat je kan spelen tegen de computer

import random

# Het bord begint als lege lijst
# Het bord heeft 9 vakjes, van linksboven naar rechtsonder
bord=[" ", " ", " ", " ", " ", " ", " ", " ", " "]

while True:
    # Wij beginnen, dus we vragen eerst de speler om input
    getal = int(input('Waar wil je een kruisje plaatsen (1-9)'))
    bord[getal-1] = "X"

    # Laten weten welke plaats we hebben gekozen
    print(f"Player chose to put an 'X' on space {getal}")

    # Hier willen we een check doen of er ergens 3 X en op een rij staan
    if bord[0] == bord[1] == bord[2] == 'X' or bord[3] == bord[4] == bord[5] == 'X' or bord[6] == bord[7] == bord[8] == 'X' or bord[0] == bord[3] == bord[6] == 'X' or bord[4] == bord[1] == bord[7] == 'X' or bord[5] == bord[8] == bord[2] == 'X' or bord[0] == bord[4] == bord[8] == 'X' or bord[4] == bord[6] == bord[2] == 'X': 
        print("Player has won!")
        break

    # Dit is een poging tot een recursieve functie die ergens een O probeert te plaatsen
    def placeo(number):
        if bord[number-1] != " ":
            global newint 
            newint = random.randint(1,9)
            placeo(newint)
        else:
            newint = number
            bord[newint-1] = "O"

    # Dan vragen we de computer om een zet te doen
    number = random.randint(1,9)
    print(f'The computer tried to put an "O" on place {number}')

    # Als hier nog niks staat, kunnen we een 'O' invullen, anders kiezen we een nieuwe
    placeo(number)

    # Laten weten welke plaats de computer heeft gekozen
    print(f"Computer chose to put an 'O' on space {newint}")
    print(f"Het bord is nu {bord}")

    # Hier een check doen of er ergens 3 O's in het spel zijn
    if bord[0] == bord[1] == bord[2] == 'O' or bord[3] == bord[4] == bord[5] == 'O' or bord[6] == bord[7] == bord[8] == 'O' or bord[0] == bord[3] == bord[6] == 'O' or bord[4] == bord[1] == bord[7] == 'O' or bord[5] == bord[8] == bord[2] == 'O' or bord[0] == bord[4] == bord[8] == 'O' or bord[4] == bord[6] == bord[2] == 'O': 
        print("Computer has won!")
        break
