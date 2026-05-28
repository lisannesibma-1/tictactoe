# Het idee is om een boter-kaas-en-eieren spel te maken dat je kan spelen tegen de computer
"""Verbeteringen ten opzichte van V4:
- Gebruik maken van Try Except
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
printbord = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]

players = int(input("How many people are playing? (1/2)"))
if players == 1:
    speler_teken = input("Do you want to play with 'O' or 'X'?").upper()
    if speler_teken == 'X':
        computer_teken = 'O'
    else:
        computer_teken = 'X'

    while True:
        try:
            # 1. Vraag om input en probeer het direct om te zetten naar een getal
            speler_zet = int(input(f'Where do you want to place a {speler_teken} (1-9)'))
        
            # 2a. Extra check: is het wel een getal tussen de 1 en 9?
            if speler_zet < 1 or speler_zet > 9:
                print("Please choose a number between 1 and 9!")
                continue # Springt direct weer naar het begin van de while-loop

            # 2b. Extra check: is het vakje al bezet
            if bord[speler_zet-1] != " ":
                print(f"You cannot put an '{speler_teken}' here!")
                continue # Springt direct weer naar het begin van de while-loop
            
        except ValueError:
            # Dit vangnet treedt in werking als int() crasht (bijv. bij letters)
            print("That is not a valid number. Please try again!")
            continue # Denk ik want nu ging het mis
        
        bord[speler_zet-1] = speler_teken
        i = (speler_zet-1)//3
        j = (speler_zet % 3)
        if j == 1 or j == 2:
            ind = j-1
        else:
            ind = 2
        printbord[i][ind] = speler_teken

        # Laten weten welke plaats we hebben gekozen
        print(f"Player chose to put an {speler_teken} on space {speler_zet}")

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
else:
    speler_teken = input("Player 1, do you want to play with 'O' or 'X'?").upper()
    if speler_teken == 'X':
        computer_teken = 'O'
    else:
        computer_teken = 'X'

    print(f"Player 1 is playing with {speler_teken}")
    print(f"Player 2 is playing with {computer_teken}")

    while True:
        invoer_is_geldig = False
    
        # Deze loop blijft draaien TOTDAT invoer_is_geldig op True wordt gezet
        while not invoer_is_geldig:
            
            # 1. Vraag om input (buiten de try)
            invoer_tekst_1 = input(f'Where do you want to place a {speler_teken} (1-9): ')
            
            # 2. Probeer om te zetten (veilig in de try)
            try:
                speler_zet = int(invoer_tekst_1)
                
                # 3. De checks (als de try lukt, komt hij hier)
                if speler_zet < 1 or speler_zet > 9:
                    print("Please choose a number between 1 and 9!")
                    # We doen niks, dus 'invoer_is_geldig' blijft False, de loop herhaalt.
                elif bord[speler_zet-1] != " ":
                    print(f"You cannot put an '{speler_teken}' here!")
                else:
                    # PAS ALS ALLES GOED IS, zetten we de schakelaar om!
                    invoer_is_geldig = True 
                    
            except ValueError:
                print("That is not a valid number. Please try again!")
                # De try is mislukt, dus de schakelaar blijft False. Hij vraagt het opnieuw.
        
        bord[speler_zet-1] = speler_teken
        i = (speler_zet-1)//3
        j = (speler_zet % 3)
        if j == 1 or j == 2:
            ind = j-1
        else:
            ind = 2
        printbord[i][ind] = speler_teken

        # Laten weten welke plaats we hebben gekozen
        print(f"Player 1 chose to put an '{speler_teken}' on space {speler_zet}")

        # Hier willen we een check doen of er ergens 3 X en op een rij staan
        if check_winst(speler_teken):
            print("Player 1 has won!")
            break

        if bord.count(" ") == 0:
            print("It's a draw!")
            break

        print("The current board:")
        for rij in printbord:
            for vakje in rij:
                print(vakje, end=' ')
            print()

        # We vragen nu speler 2 om input. Voor simplicity houden we computer_zet aan als de zet van speler 2
        invoer_is_geldig = False
    
        # Deze loop blijft draaien TOTDAT invoer_is_geldig op True wordt gezet
        while not invoer_is_geldig:
            
            # 1. Vraag om input (buiten de try)
            invoer_tekst_2 = input(f'Where do you want to place a {computer_teken} (1-9): ')
            
            # 2. Probeer om te zetten (veilig in de try)
            try:
                computer_zet = int(invoer_tekst_2)
                
                # 3. De checks (als de try lukt, komt hij hier)
                if computer_zet < 1 or computer_zet > 9:
                    print("Please choose a number between 1 and 9!")
                    # We doen niks, dus 'invoer_is_geldig' blijft False, de loop herhaalt.
                elif bord[computer_zet-1] != " ":
                    print(f"You cannot put an '{computer_teken}' here!")
                else:
                    # PAS ALS ALLES GOED IS, zetten we de schakelaar om!
                    invoer_is_geldig = True 
                    
            except ValueError:
                print("That is not a valid number. Please try again!")
                # De try is mislukt, dus de schakelaar blijft False. Hij vraagt het opnieuw.

        bord[computer_zet-1] = computer_teken
        i = (computer_zet-1)//3
        j = (computer_zet % 3)
        if j == 1 or j == 2:
            ind = j-1
        else:
            ind = 2
        printbord[i][ind] = computer_teken

        # Laten weten welke plaats we hebben gekozen
        print(f"Player 2 chose to put an '{computer_teken}' on space {computer_zet}")

        # Hier willen we een check doen of er ergens 3 X en op een rij staan
        if check_winst(computer_teken):
            print("Player 2 has won!")
            break

        print("The current board:")
        
        for rij in printbord:
            for vakje in rij:
                print(vakje, end=' ')
            print()