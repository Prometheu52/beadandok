# ---------+---------+-----Import----+---------+----------
import sys
# ---------+---------+-----System arguments----+---------+----------
n = sys.argv[1]
while True:
    try:
        n = int(n)
        break
    except ValueError:
        print("Hibás system argument!\nNem lehet int formába alakítani.")
        sys.exit(-1)
szo = sys.argv[2]
# ---------+---------+-----Mag----+---------+----------
ki = ""
# Feltölti az első n elemet
x = 1
for i in range(n):
    ki += szo[i]*x
    x += 1
# Feltölti n-től visszafele haladva
x -= 1
for i in range(n, len(szo)):
    x -= 1
    ki += szo[i]*x
# ---------+---------+-----Kiiratás----+---------+----------
print(ki)
