"""
instance attributumok - self szó használva van
class attributum (osztály változó) - cls szó van használva
a class attributum használatához nem szükséges objektumot létrehozni
a class változó értékét, ha a classon keresztül módosítom, akkor minden objekt, ami a classból 
példányosotott ezt az új értéket kapja meg

class method:
nem látja az instance attributumokat

cls kulcsszó segíségével eléri az osztály attributumokat - az attributum mindent jelent: változ és függvény egyaránt

mire jó:
az osztály állapotának megváltoztatására
attributumainak megváltoztatására

Instance attributumok a self kulcsó használatával is el tudjáj érni a class attributumokat

"""

class TestClass:
    file_path = None
    def __init__(self):
        self.name = "Pisti"

    def valami(self):
        self.name = "Valami"

    # class variable
    value = 10

test = TestClass()
test2 = TestClass()

TestClass.value = 400


# print(test.value)
# print(test2.value)

# figyelni kell a következőre

test3 = TestClass()

test3.value = 10_000

test3.value = TestClass.value
# print(test.value)
# print(test2.value)
# print(test3.value)


class TestClass:
    # class variable
    name = "Karcsi"
    def __init__(self):
        self.value = 10_000

    @classmethod
    def my_cls_func(cls, param1=None):
        cls.kiir()

    @classmethod
    def kiir(cls):
        print(f"hello {cls.name}")

test = TestClass()

# test.my_cls_func()


class Person:
    temp = "valami"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birthday(cls, name, year):
        from datetime import date
        return cls(name, date.today().year - year)

    def cre_obj_from_birthday(self, name, year):
        from datetime import date
        return Person(name, date.today().year - year)
    
    def my_test(self):
        print(Person.temp)
        print(self.temp)
        self.cre_obj_from_birthday("Pista", 2003)

ricsi = Person("Ricsi", 50)
ricsi = ricsi.cre_obj_from_birthday("Ricsi", 1990)
ricsi_with_year = Person.from_birthday("Ricsi", 1990)

ricsi.my_test()


class TestClass:
    temp = 100
    def __init__(self):
        self.temp = 100

    @classmethod
    def change_temp(cls, value):
        cls.temp = value
        # TestClass.temp = value

    @staticmethod
    def stat_change_temp(class_definition, value):
        class_definition.temp = value

    def ins_change_temp(self, class_definition, value):
        class_definition.temp = value

test = TestClass()
test2 = TestClass()

TestClass.temp = 500
TestClass.stat_change_temp(TestClass, 1400)

print(test.temp)
print(test2.temp)