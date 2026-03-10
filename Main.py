import random
from collections import Counter

Ruch_Gracz1 = 0
Wynik_Gracz1 = 0
Ruch_Gracz2 = 0
Wynik_Gracz2 = 0

K1_Gracz1 = [None, None, None]
K2_Gracz1 = [None, None, None]
K3_Gracz1 = [None, None, None]
K1_Gracz2 = [None, None, None]
K2_Gracz2 = [None, None, None]
K3_Gracz2 = [None, None, None]

def policz_wynik(kolumny):
    total = 0
    for kol in kolumny:
        liczby = [x for x in kol if x is not None]
        liczby_licznik = Counter(liczby)
        for liczba, ile_razy in liczby_licznik.items():
            total += liczba * ile_razy * ile_razy  # <-- każda kostka mnożona przez ilość powtórzeń
    return total

while True:
    '''
    GRACZ 1
    '''
    print()

    Oczka_Gracz1 = random.randint(1, 6)
    print("Gracz 1 wylosował: ", Oczka_Gracz1)

    Ruch_Gracz1 = int(input("Gdzie położyć kostkę? (kolumna 0-3): "))

    if Ruch_Gracz1 == 1:
        if K1_Gracz1[0] is None: K1_Gracz1[0] = Oczka_Gracz1
        elif K1_Gracz1[1] is None: K1_Gracz1[1] = Oczka_Gracz1
        elif K1_Gracz1[2] is None: K1_Gracz1[2] = Oczka_Gracz1
        else: print("Brak możliwości położenia tam kostki")
    if Ruch_Gracz1 == 2:
        if K2_Gracz1[0] is None: K2_Gracz1[0] = Oczka_Gracz1
        elif K2_Gracz1[1] is None: K2_Gracz1[1] = Oczka_Gracz1
        elif K2_Gracz1[2] is None: K2_Gracz1[2] = Oczka_Gracz1
        else: print("Brak możliwości położenia tam kostki")
    if Ruch_Gracz1 == 3:
        if K3_Gracz1[0] is None: K3_Gracz1[0] = Oczka_Gracz1
        elif K3_Gracz1[1] is None: K3_Gracz1[1] = Oczka_Gracz1
        elif K3_Gracz1[2] is None: K3_Gracz1[2] = Oczka_Gracz1
        else: print("Brak możliwości położenia tam kostki")

    print(K1_Gracz1)
    print(K2_Gracz1)
    print(K3_Gracz1)

    Kolumny_Gracz1 = [K1_Gracz1, K2_Gracz1, K3_Gracz1]
    Wynik_Gracz1 = policz_wynik(Kolumny_Gracz1)
    print("Gracz 1: ", Wynik_Gracz1, " pkt")


    if None not in K1_Gracz1 + K2_Gracz1 + K3_Gracz1:
        print("\nKoniec gry!")
        if Wynik_Gracz1 > Wynik_Gracz2: print("Wygrywa gracz 1!")
        elif Wynik_Gracz1 < Wynik_Gracz2: print("Wygrywa gracz 2!")
        else: print("Remis!")
        break
    else:
        '''
        GRACZ 2
        '''

        print()

        Oczka_Gracz2 = random.randint(1, 6)
        print("Gracz 2 wylosował: ", Oczka_Gracz2)

        Ruch_Gracz2 = int(input("Gdzie położyć kostkę? (kolumna 0-3): "))

        if Ruch_Gracz2 == 1:
            if K1_Gracz2[0] is None: K1_Gracz2[0] = Oczka_Gracz2
            elif K1_Gracz2[1] is None: K1_Gracz2[1] = Oczka_Gracz2
            elif K1_Gracz2[2] is None: K1_Gracz2[2] = Oczka_Gracz2
            else: print("Brak możliwości położenia tam kostki")
        if Ruch_Gracz2 == 2:
            if K2_Gracz2[0] is None: K2_Gracz2[0] = Oczka_Gracz2
            elif K2_Gracz2[1] is None: K2_Gracz2[1] = Oczka_Gracz2
            elif K2_Gracz2[2] is None: K2_Gracz2[2] = Oczka_Gracz2
            else: print("Brak możliwości położenia tam kostki")
        if Ruch_Gracz2 == 3:
            if K3_Gracz2[0] is None: K3_Gracz2[0] = Oczka_Gracz2
            elif K3_Gracz2[1] is None: K3_Gracz2[1] = Oczka_Gracz2
            elif K3_Gracz2[2] is None: K3_Gracz2[2] = Oczka_Gracz2
            else: print("Brak możliwości położenia tam kostki")

        print(K1_Gracz2)
        print(K2_Gracz2)
        print(K3_Gracz2)

        Kolumny_Gracz2 = [K1_Gracz2, K2_Gracz2, K3_Gracz2]
        Wynik_Gracz2 = policz_wynik(Kolumny_Gracz2)
        print("Gracz 2: ", Wynik_Gracz2, " pkt")

        if None not in K1_Gracz1 + K2_Gracz1 + K3_Gracz1:
            print("\nKoniec gry!")
            if Wynik_Gracz1 > Wynik_Gracz2: print("Wygrywa gracz 1!")
            elif Wynik_Gracz1 < Wynik_Gracz2: print("Wygrywa gracz 2!")
            else: print("Remis!")
            break