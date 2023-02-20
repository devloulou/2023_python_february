# import modul

"""
Built-In szint

pl. len(), min(), max(), list(), dict()....etct.
"""

# print(__builtins__)

#ez a global namespace

my_list = [1, 2, 3, 4]

a = 120
def my_func():
    # ez a local namespace    
    global a
    a = 130


# my_func()

# print(a)

b = 20

def my_func():
    # ez az enclosing namepace
    b = 10

    def wrapper():
        # local namespace
        c = 10
        nonlocal b
        b = 300

    wrapper()
    print(b)

my_func()