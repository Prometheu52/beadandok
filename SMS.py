# ---------+---------+-----Imports----+---------+---------
import numpy as np
# ---------+---------+---------+---------+---------
# Értékvizsgálat
while True:
    bekeresek_szama = input("Beolvasandó sorok száma: ")
    try:
        bekeresek_szama = int(bekeresek_szama)
        break
    except ValueError:
        print("Hibás érték!\nEgész számot adj meg!")
# ---------+---------+-----Mátrix feltöltése----+---------+---------
m = np.empty((bekeresek_szama, 4), dtype='U40')
for i in range(bekeresek_szama):
    msg = ""
    # Értékvizsgálat
    while True:
        x = input("Sor: ").split(" ")
        if len(x) < 4:
            print("Rossz input, add meg újra!")
        else:
            break
    # Üzenet összerakása
    for j in range(3, len(x)):
        msg += x[j]
        msg += " "
    # Mátrix összerakása
    for z in range(3):
        m[i][z] = x[z]
    m[i][3] = msg[0:len(msg)-1]
# ---------+---------+-----Mártix csoportosítása(telefonszám, idő)----+---------+-------
for i in range(bekeresek_szama-1):
    for j in range(i+1, bekeresek_szama):
        if m[i][0] == m[j][0]:
            m[[i+1, j]] = m[[j, i+1]]
            # print(f'{i},{j}')
            if int(m[i][1]+m[i][2]) > int(m[i+1][1]+m[i+1][2]):
                m[[i, i+1]] = m[[i+1, i]]
# ---------+---------+-----Output----+---------+---------
text = open('SMS.txt', 'w')
tszam = 1
for i in range(bekeresek_szama):
    if m[i-1][0] == m[i][0] and i != 0:
        tszam += 1
        text.write(f'\t{tszam}. {m[i][1]} {m[i][2]} {m[i][3]}\n')
    else:
        tszam = 1
        text.write(f'{m[i][0]}:\n')
        text.write(f'\t{tszam}. {m[i][1]} {m[i][2]} {m[i][3]}\n')
text.close()
print("AZ eredmény az SMS.txt -ben található!")