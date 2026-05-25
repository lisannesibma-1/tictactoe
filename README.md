Boter, kaas en eieren, wie ken het niet?
Bord:
1 2 3
4 5 6
7 8 9

V1: Speler kiest een getal en speelt daar een 'X' en de computer kiest een random getal van 1 tot en met 9 en als deze plek nog leeg is, speelt de computer daar een 'O'.
    Als één van de spelers 3 dezelfde tekens op een rij heeft, is er een winnaar!

V2: De veranderingen in deze versie zijn vooral gericht op de mechanieken van het spel:
- De computer is slimmer: Hij probeert eerst zelf te winnen, daarna de speler te blokkeren en kiest anders uit de overgebleven lege vakjes willekeurig
- De winnende lijnen zijn overzichtelijker gemaakt, zodat de code makkelijker te lezen is
- Er is een mogelijkheid tot gelijkspel

V3: De veranderingen in deze versie zijn vooral cosmetisch:
- Het bord wordt niet meer slechts als lijst geprint, maar als 3x3 grid
- De speler kan kiezen met welk teken die wilt spelen

V4: De veranderingen in deze versei zijn:
- Het wordt mogelijk om in plaats van tegen de computer, tegen een andere tegenstander te spelen
- Daarnaast kan er geen zet meer gespeeld worden op een vakje dat al bezet is

### Python Concepts:
* **2D Matrix Datastructuren:** Speelveld-architectuur via geneste lijsten (`[rij][kolom]`) en data-validatie met `while`-loops.
* **Wiskundige Logica:** Input-transformatie met integer division (`//`) en matrix-coördinatie.
* **Algoritmische AI:** Strategische beslissingsboom voor de computer-tegenstander (Winnen -> Blokkeren -> Willekeurig).
