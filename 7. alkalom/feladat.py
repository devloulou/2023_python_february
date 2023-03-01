""" A feladat:
Dracula.txt file-ról készítünk statisztikát
statisztikák:
    leghosszab sor
    állapítsuk meg, hogy hány oldala van: 3000 karakter ~ 1 oldal
    legrövidebb sor
    leggyakrabban előforduló 5 szó: szónak tekintem azt, ami legalább 5 karakter hosszú

Amikor a statisztikák elkészültek, írjuk ki az eredményt egy JSON file-ba, aminek legyen a neve:
statistics.json
"""

"""
A megoldáshoz vezető út:
1. ki kell nyernem az adatot a txt-ből
2. statisztika készítés
3. statisztika kiírása JSON-be

"""
# speficikus
def my_func(a, b, c, d):
    temp = [a, b, c, d]
    return max(temp)

# print(my_func(1, 2, 3, 4))

def my_func(*args):
    return max(args)

# print(my_func(1, 2, 3, 4, 10, 10, 30))