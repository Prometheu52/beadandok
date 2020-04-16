# ---------+---------+-----Imports----+---------+---------
import numpy as np
import sys
# ---------+---------+---------+---------+---------

# ---------+---------+----Tömbök-----+---------+---------
# Címletek
ermek = np.array([1, 5, 100, 50, 2, 10])
# ermek = np.array([100, 50, 10, 5, 2, 1])

# Reprezentatív tömb
visszajaro_t = np.zeros(6, dtype='int')
# ---------+---------+---------+---------+---------

# ---------+---------+----Ismétlések bekérése-----+---------+---------
while True:
    ismetlesk_szama = input("Ismétlések száma: ")
    try:
        ismetlesk_szama = int(ismetlesk_szama)
        if ismetlesk_szama <= 0:
            print("Nem lehet nulla vagy negatív... -.-")
            continue
        break
    except ValueError:
        print("Egész számot adj meg értéknek!")
# ---------+---------+---------+---------+---------


def visszajaro(cimletek, reprez_t):
    """A program megadja hogy egy kapott összeget hogyan lehet a legkevesebb darabszámú címlettel visszaadni. A
    címletek egy csökkenő sorrendben rendezett lista mely tartalmazza a címleteket. Lehetőség van rá hogy a program
    automatikusan rendezze azt. Az inputokat standard inputól olvassa be."""
    # ---------+---------+-----Címlet tömb ellenőrzése-----+----------+---------
    # Megvizsgálja hogy jó-e a rendezés, ha nem akkor az x átvált így belemegy az ezt követő if-be
    x = False
    for i in range(len(cimletek) - 1):
        if cimletek[i] < cimletek[i + 1]:
            x = True
            break
    if x:
        # Értékmegadás helyességét vizsgálja -> rendezze-e
        while True:
            rendezze_e = input("A címleteket tartalmazó tömb rendezése nem megfelelő!\nSzeretné hogy automatikusan "
                               "rendezve legyen?(i/n)").lower()
            if rendezze_e == "i" or rendezze_e == "n":
                break
            else:
                print("\nA megadott érték nem ismerhető fel, add meg újra!\n")
        if rendezze_e == 'i':
            # Rendezés -> maximum kiválasztásos (O(N**2))
            for i in range(len(cimletek)):
                max = 0
                indx = 0
                for j in range(i, len(cimletek)):
                    if cimletek[j] > max:
                        max = cimletek[j]
                        indx = j
                if cimletek[i] < max:
                    cimletek[i], cimletek[indx] = cimletek[indx], cimletek[i]
            print(cimletek)
        else:
            # Kilép a programból -> ne kérdezze meg input-számszor a rendezést hamár egyszer elutasítottuk
            # 0 mert hiba nékül lefutott
            print("A tömb rendezése rossz!")
            sys.exit(0)
    # ---------+---------+-----Reprezentáló tömb nullázása-----+----------+---------
    # Ha nem tesszük akkor az előző eredmény benne maradna
    for i in range(len(reprez_t)):
        reprez_t[i] = 0
    # ---------+---------+-----Értékvizsgálat-----+----------+---------
    # A pénz input helyesség ellenőrzése
    while True:
        penz = input("Kapott összeg: ")
        try:
            penz = int(penz)
            if penz <= 0:
                print("Nem lehet nulla vagy negatív... -.-")
                continue
            break
        except ValueError:
            print("Egész számot adj meg értéknek!")
    # ---------+---------+-----Mag-----+----------+---------
    # Visszajáró kiszámolása
    for i in range(len(cimletek)):
        while penz / cimletek[i] >= 1:
            reprez_t[i] += 1
            penz -= cimletek[i]
        if penz == 0:
            break
    # ---------+---------+-----Kiiratás-----+----------+---------
    # A kapott eredmény kiírása
    for i in range(len(cimletek)):
        if reprez_t[i] != 0:
            print(f'{reprez_t[i]}db {cimletek[i]}Ft', end="; ")


# ---------+---------+-----Feladat----+---------+---------
for i in range(ismetlesk_szama):
    visszajaro(ermek, visszajaro_t)
# ---------+---------+---------+---------+---------

# ---------+---------+-----Jegyzetek / Hibák----+---------+---------

