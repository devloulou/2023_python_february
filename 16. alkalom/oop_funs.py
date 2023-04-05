
class Test:
    def __init__(self):
        self.name = None


test = Test()
# test.nme = "Amanda"

# print(test.name)


class Test:
    pass

test = Test()

test.age = 10

def greetings():
    print("Hi Ricsi")

test.my_func = greetings

test.my_func()


"""
kell e mindig __init__ metódus?
Nem minden esetben kell construktor - __init__ metódus

a self azért kell minden esetben az instance attributumokhoz - függvényekről beszélek -
mert alapből a python magát az objektumot odaadja mint referencia a használt függvénynek

construktornak van egy ellen párja - destructor: megszűnteti és felszabadítja a memória területét
az instance változóknak -> pythonban nem  kell ilyet tenned

Python memória managementje dinamikus  és az objektumok élettartamát a garbage collector vezérli

"""

class Test:
    def __init__(self):
        pass

    def say_hi(self):
        print("szia")

test = Test()

test.say_hi()

