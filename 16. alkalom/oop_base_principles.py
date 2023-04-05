"""
OOP - Object Oriented Programming - Objektum Orientált Programozás
osztályokat létrehozni, amelyekből objektumokat fogunk példányosítani

az OOP az nem a cél

4 alapelv  - 4 principle:

abstraction - absztrakció
inheritencia - öröklődés
encapsulation - egységbe zárás
polimorphism - többalakúság

"""
# myClass
# MyClass - ez python nevezéktan ajánlás

class MyClass:
    pass

"""
Abstraction - rejtsd el a kódot a használat helyétől
"""

def my_func(name: str, age: int):
    ...


class Human:
    """
    egy osztálynak attribútumai vannak - tulajdonságok: változók, függvények és osztályok
    
    __init__() - az osztály konstruktora: 
        a kívülről érkező attributumokat ha elérhetővé szeretném tenni az osztály számára
        ha alap tuljadonságokat szeretnél beállítani - változókra gondolok, 
        ha a példányosítás során azt szeretném, hogy bizonyos folyamatok automatikusan elinduljanak
    
    classon belül minden függvényre igaz: az első paramétere fix, pozíció alapon: self kulcsszó
    
    self egy ajánlás, hogy ez legyen a neve: lehet bármi

    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.employed = True
        self.iq = 120
        # self.greetings()
    
    def greetings(self):
        print(f"HI, {self.name}")


erno = Human('Ernő', 40)
kati = Human('Kati', 23)


# kati.greetings()


"""
inheritencia - öröklődés

szülő (ős)- gyermek kapcsolat kialakítása 2 osztály között
Python le tudja kezelni a többszörös öröklődést -> gyermek osztálynak több ős osztálya van

öröklődés: a gyermek osztály az ős osztály minden attribumát: változóit, függvényeit leszármaztatja, 
            a gyermek osztály tudja az ős osztály minden tulajdonságát használni és módosítani
"""

# ő az ős osztály
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Szia {self.name}")


class Woman(Human):
    def __init__(self, name, age):
        # supercharge ősosztályt
        super().__init__(name, age)
        self.sex = "woman"

    def greetings(self):
        print(f"Hello {self.name} vagyok és {self.age} éves")


class Man(Human):
    def __init__(self, name, age):
        # supercharge ősosztályt
        super().__init__(name, age)
        self.sex = "man"

reni = Woman("Reni", 19)
karcsi = Man("Karcsi", 50)

# reni.greetings()
# karcsi.greetings()

# print(reni.sex)

"""
self kulcsszó az mindig a példányosított objektumra hivatkozik
minden self-el ellátott függvény magához az objektumhoz tartozik
és minden self kulcsszóval ellátott attributum egy instance attributum

"""

"""
Encapsulation - egységbe zárás
Minden az objektumhoz tartozó attributum legyen private addig, amíg nem kell publikusan elérhetőnek
lennie.

Private attributum: kívülről semmilyen formában nem tudod az értékét a private attributumnak
    - lekérni
    - módosítani

A pythonban nincs olyan, hogy private
object._Osztálynév__változóneve

osztályon belüli attribútum láthatósága
publikus, private

c# - protected

"""

class Test:
    # __funcname__ típusú függvények a magic methodoc, double underscore methods, dunderscore
    def __init__(self):
        self.__myval = 100 
        self.a = "alma"

t = Test()
t._Test__myval = 300
# print(t._Test__myval)


"""
Polimorphism - többalakúság
"""

# polimorph függvények: len()

my_string = "almafa"
my_list =  [1, 2, 3, 4, 5]
my_dict = {
    "key": "value"
}

print(len(my_string))
print(len(my_list))
print(len(my_dict))

class India:
    def language(self):
        print("Indians speak Hindi")

    def landsize(self):
        print("India is very very big")


class Hungary:
    def language(self):
        print("Hungarians speak Hungarian")

    def landsize(self):
        print("Hungary is very very small")


india = India()
hun = Hungary()

temp = (india, hun)

for item in temp:
    item.landsize()
    item.language()