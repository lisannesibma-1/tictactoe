# Het idee is om een boter-kaas-en-eieren spel te maken dat je kan spelen tegen de computer
"""Verbeteringen ten opzichte van V2:
- betere print van het bord
- speler mag kiezen met welk teken hij speelt
"""
import random
import math

def check_winst(speler_teken):
    # Alle 8 mogelijke manieren om te winnen (rijen, kolommen, diagonalen)
    winnende_lijnen = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontaal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Verticaal
        [0, 4, 8], [2, 4, 6]             # Diagonaal
    ]
    
    # Loop door elke lijn heen en check of alle drie de vakjes het teken hebben
    for lijn in winnende_lijnen:
        if bord[lijn[0]] == bord[lijn[1]] == bord[lijn[2]] == speler_teken:
            return True # Er is een winnaar!
            
    return False # Nog geen winnaar

def vind_slimme_zet(computer_teken, speler_teken):
    winnende_lijnen = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # STAP 1: Kan de computer NU winnen?
    for lijn in winnende_lijnen:
        vakjes = [bord[lijn[0]], bord[lijn[1]], bord[lijn[2]]]
        # Als er 2 O's staan en 1 lege plek
        if vakjes.count(computer_teken) == 2 and vakjes.count(" ") == 1:
            leeg_index = lijn[vakjes.index(" ")]
            return leeg_index + 1 # +1 omdat jouw systeem met 1-9 werkt

    # STAP 2: Moet de computer de speler blokkeren?
    for lijn in winnende_lijnen:
        vakjes = [bord[lijn[0]], bord[lijn[1]], bord[lijn[2]]]
        # Als de speler 2 X'en heeft en er is 1 lege plek
        if vakjes.count(speler_teken) == 2 and vakjes.count(" ") == 1:
            leeg_index = lijn[vakjes.index(" ")]
            return leeg_index + 1

    # STAP 3: Geen directe winst of blokkade? Kies een willekeurige vrije plek
    vrije_plekken = [i + 1 for i, vakje in enumerate(bord) if vakje == " "]
    if vrije_plekken == []:
        return 'gelijkspel'
    else:
        return random.choice(vrije_plekken)

# Het bord begint als lege lijst
# Het bord heeft 9 vakjes, van linksboven naar rechtsonder
bord=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
printbord = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

speler_teken = input("Do you want to play with 'O' or 'X'?").upper()
if speler_teken == 'X':
    computer_teken = 'O'
else:
    computer_teken = 'X'

while True:
    # Wij beginnen, dus we vragen eerst de speler om input
    getal = int(input('Waar wil je een kruisje plaatsen (1-9)'))
    bord[getal-1] = speler_teken
    i = (getal-1)//3
    j = (getal % 3)
    if j == 1 or j == 2:
        ind = j-1
    else:
        ind = 2
    print(f"i = {i}")
    print(f"ind = {ind}")
    printbord[i][ind] = speler_teken

    # Laten weten welke plaats we hebben gekozen
    print(f"Player chose to put an {speler_teken} on space {getal}")

    # Hier willen we een check doen of er ergens 3 X en op een rij staan
    if check_winst(speler_teken):
        print("Player has won!")
        break

    # BEURT VAN DE COMPUTER
    # De slimme functie berekent de beste plek (geeft getal 1-9 terug)
    computer_zet = vind_slimme_zet(computer_teken, speler_teken)
    if computer_zet == 'gelijkspel':
        print("It's a draw!")
        break

    bord[computer_zet - 1] = computer_teken
    k = (computer_zet-1)//3
    l = (computer_zet % 3)
    if l == 1 or l == 2:
        inde = l-1
    else:
        inde = 2
    print(f"k = {k}")
    print(f"inde = {inde}")
    printbord[k][inde] = computer_teken

    
    print(f"Computer chose to put an {computer_teken} on space {computer_zet}")
    print("The current board:")
    
    for rij in printbord:
        for vakje in rij:
            print(vakje, end=' ')
        print()


    # Hier een check doen of er ergens 3 O's in het spel zijn
    if check_winst(computer_teken):
        print("Computer has won!")
        break