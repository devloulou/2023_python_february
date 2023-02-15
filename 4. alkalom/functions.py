"""
Functions - függvények, metódusok

kivétel: lambda függvény -> functional programming (lambda, map stb.)

def fuggveny_neve(parameterek):
    a függvény belseje: különböző utasítások
    [return value]

Minden függvénynek van visszatérési értéke, függetlenül attól,
hogy én rendelkezek róla, vagy nem

ha nem rendelkezem visszatérési értékről, akkor minden esetben None-al tér vissza

a függvény is egy objektum

return utasítás:
megállítja a függvény futását
"""

def my_func():
    print("Hello")

# példányosítás, függvény futtatás

def my_func():
    print(2+3)

def my_func():
    return 5, 6, 7, 8    


# függvények paraméterei
# vesszővel elválasztott paraméterek kötelező argumentumai a függvénynek
def add_numbers(num1, num2):
    return num1 + num2

temp = add_numbers

# print(temp(5, 6))

# default értékadás argumentumoknak (kezdőérték)
def add_numbers(num1=10, num2=20):
    return num1 + num2

temp = add_numbers(5, 7)

temp = add_numbers(num2=30, num1=5)

# print(add_numbers())
# print(temp)
"""

my_func(num1);
my_func(num1, num2);
my_func(num1, num2, num3);
my_func(num1, num2, my_str);

my_func(5);
my_func(5, 6);
my_func(5, 6, 7);
my_func(4, 5, "Ricsi");

"""
def my_func(a, b):
    return a + b
    

def my_func(a, b, c):
    return a - b + c

# polymorph függvény

# def len(param):
#     cnt = 0
#     for i in param:
#         cnt += 1
#     return cnt

# print(len("Ricsi"))
# print(len([1, 2, 3, 4]))
# print(len({"kulcs": "érték"}))

# "function overloading"
# packing & unpacking
# az args nem kötelező név
def my_func(*args):
    ...
    # print(args)

# positinal argumentumok
my_func(1, 2, 3, 5,6 , [123123124, "Ricsi"])


# **kwargs - keywords arguments
# az kwargs nem kötelező név
def my_func(**kwargs):
    pass
    ...
    # print(kwargs.get('shp'))
    # print(kwargs)

my_func(name="Ricsi", age=32, occupation="big data engineer")

# *args, **kwargs

def my_func(*args, **kwargs):
    print(args)
    print(kwargs)

my_func(1, 2, 3, 4, 5, name="Ricsi")