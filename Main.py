import random
from collections import Counter


def policz_wynik(kolumny):
    total = 0
    for kol in kolumny:
        liczby = [x for x in kol if x is not None]
        licznik = Counter(liczby)

        for liczba, ile in licznik.items():
            total += liczba * ile * ile

    return total


def wstaw_kostke(kolumny, kolumna, oczka):
    kol = kolumny[kolumna]

    for i in range(3):
        if kol[i] is None:
            kol[i] = oczka
            return

    print("Brak możliwości położenia tam kostki")


def plansza_pelna(kolumny):
    return None not in sum(kolumny, [])


def tura(gracz, kolumny):
    print()

    oczka = random.randint(1, 6)
    print(f"Gracz {gracz} wylosował:", oczka)

    ruch = int(input("Gdzie położyć kostkę? (kolumna 1-3): ")) - 1

    if 0 <= ruch < 3:
        wstaw_kostke(kolumny, ruch, oczka)

    for kol in kolumny:
        print(kol)

    wynik = policz_wynik(kolumny)
    print(f"Gracz {gracz}: {wynik} pkt")

    return wynik


kolumny_gracz1 = [[None]*3 for _ in range(3)]
kolumny_gracz2 = [[None]*3 for _ in range(3)]

wynik1 = 0
wynik2 = 0


while True:

    wynik1 = tura(1, kolumny_gracz1)

    if plansza_pelna(kolumny_gracz1):
        break

    wynik2 = tura(2, kolumny_gracz2)

    if plansza_pelna(kolumny_gracz2):
        break


print("\nKoniec gry!")

if wynik1 > wynik2:
    print("Wygrywa gracz 1!")
elif wynik1 < wynik2:
    print("Wygrywa gracz 2!")
else:
    print("Remis!")