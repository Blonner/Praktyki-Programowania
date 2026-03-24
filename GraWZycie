import random
import time
import os

RZEDY = 20
KOLUMNY = 20


def tworzenie_siatki():
    tab = []
    for i in range(RZEDY):
        wiersz = []
        for j in range(KOLUMNY):
            wiersz.append(random.choice([0, 1]))
        tab.append(wiersz)
    return tab


def wyswietl(siatka):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(RZEDY):
        for j in range(KOLUMNY):
            komorka = siatka[i][j]
            print('X' if komorka == 1 else '.', end="")  #
        print()
    print("============================")

def sasiedzi(siatka, r, k):
    licznik = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            sasiad_r = (r + i) % RZEDY
            sasiad_k = (k + j) % KOLUMNY

            if siatka[sasiad_r][sasiad_k] == 1:
                licznik += 1
    return licznik


def nowe_pokolenie(siatka):

    nowa_siatka = [[0 for _ in range(KOLUMNY)] for _ in range(RZEDY)]
    for r in range(RZEDY):
        for k in range(KOLUMNY):
            ilosc_sasiadow = sasiedzi(siatka, r, k)
            if siatka[r][k] == 1:
                if ilosc_sasiadow == 2 or ilosc_sasiadow == 3:
                    nowa_siatka[r][k] = 1
                else:
                    nowa_siatka[r][k] = 0
            else:
                if ilosc_sasiadow == 3:
                    nowa_siatka[r][k] = 1
    return nowa_siatka


def main():
    siatka = tworzenie_siatki()

    while True:
        wyswietl(siatka)
        siatka = nowe_pokolenie(siatka)
        time.sleep(1)


if __name__ == '__main__':
    main()
