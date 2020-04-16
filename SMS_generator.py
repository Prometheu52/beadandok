import numpy as np
import random
b = ["JAN ", "FEB", "M O Z A R T", "Sajtot szósszal", "Tejet kekkszekel", "Szósszal paradicsomosal", "Olajos mártással"]
# elso = "9" masodik = "2" harmadik = "2" string = "40"
telszam = np.empty(4, dtype=object)
for i in range(4):
    tsz = ""
    for j in range(9):
        tsz += str(random.randint(0, 9))
    telszam[i] = tsz
f = open("47Generator.txt", "w")
for i in range(10):
    sms = ""
    sms = telszam[random.randint(0, 3)] + " " + str(random.randint(0, 2))+str(random.randint(0, 4)) + " " + str(random.randint(0, 9)) + str(random.randint(0, 9))+" "
    sms += " " + b[random.randint(0, 6)]
    print(sms)
    sms += "\n"
    f.write(sms)
print("\n47Generator.txt Created")



