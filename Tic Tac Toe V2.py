# Het idee is om een boter-kaas-en-eieren spel te maken dat je kan spelen tegen de computer
"""Verbeteringen ten opzichte van V1:
- winnende lijnen overzichtelijker in de code gemaakt
- computer speelt slimmer en niet willekeurig
- er is een mogelijkheid tot gelijkspel
"""
import random

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

while True:
    # Wij beginnen, dus we vragen eerst de speler om input
    getal = int(input('Waar wil je een kruisje plaatsen (1-9)'))
    bord[getal-1] = "X"

    # Laten weten welke plaats we hebben gekozen
    print(f"Player chose to put an 'X' on space {getal}")

    # Hier willen we een check doen of er ergens 3 X en op een rij staan
    if check_winst("X"):
        print("Player has won!")
        break

    # BEURT VAN DE COMPUTER
    # De slimme functie berekent de beste plek (geeft getal 1-9 terug)
    computer_zet = vind_slimme_zet("O", "X")
    if vind_slimme_zet("O", "X") == 'gelijkspel':
        print("It's a draw!")
        break

    bord[computer_zet - 1] = "O"
    print(f"Computer chose to put an 'O' on space {computer_zet}")
    print(f"Het bord is nu: {bord}")

    # Hier een check doen of er ergens 3 O's in het spel zijn
    if check_winst("O"):
        print("Computer has won!")
        break