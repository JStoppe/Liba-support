print("willkommen zum Zahlenraten")

import random
zahl = random.randint(1, 10)

richtig = False

for i in range(3):
    dieZahl = int(input("schreib eine Zahl von 1 bis 10:"))
    if dieZahl == zahl:
        print("richtig du hast gewonnen")
        richtig = True
        break
    elif dieZahl < zahl:
        print("etwas mehr!")
    else:
        print("etwas weniger!")

if not richtig:
    print(zahl)
