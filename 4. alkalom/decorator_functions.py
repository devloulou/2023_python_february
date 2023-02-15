"""
Decorator függvény:

@decorator_func_name
def my_func():
    ...

A decorator függvény egy olyan speciális függvény,
amely anélkül ad plusz tulajdonságot egy függvényvéhez, hogy az
változatna a függvény működésén, paraméterein és a definícióján

logolás
hibakezelés
futási idő és egy metrikák mérésére
register
caching mechanizmus
lassítani a futáson

"""


def calculator(num1, num2, operator):

    def add(a, b):
        return a + b

    def kivonas():
        return num1 - num2
    
    def power():
        return num1 * num2
    
    def division():
        return num1 / num2 
    
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return kivonas()
    elif operator == '*':
        return power()
    elif operator == '/':
        return division()
    else:
        print("Nincs ilyen művelet")


# print(calculator(2, 3, "+"))


def start_end_decor(func):
    def wrapper():
        # előtte is tudok csinálni dolgokat
        print("Start")
        func()
        print("End")
        # utána is tudok csinálni dolgokat
    return wrapper

def my_func():
    start = 10
    while start >= 0:
        print(f"{start}")
        start -= 1

@start_end_decor
def my_func():
    start = 10
    while start >= 0:
        print(f"{start}")
        start -= 1

# my_func()

# start_end_decor(my_func)

def start_end_decor(func):
    def wrapper(*args, **kwargs):
        # előtte is tudok csinálni dolgokat
        print("Start")
        retval = func(*args, **kwargs)        
        # utána is tudok csinálni dolgokat
        return retval
    return wrapper

@start_end_decor
def calculator(num1, num2, operator):

    def add(a, b):
        return a + b

    def kivonas():
        return num1 - num2
    
    def power():
        return num1 * num2
    
    def division():
        return num1 / num2 
    
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return kivonas()
    elif operator == '*':
        return power()
    elif operator == '/':
        return division()
    else:
        print("Nincs ilyen művelet")


# value = calculator(2, 3, "+")

# print(value)


@start_end_decor
def my_func():
    start = 10
    while start >= 0:
        print(f"{start}")
        start -= 1

# my_func()



#####################################################################

def repeat(cnt):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            retval = 0
            for _ in range(cnt):
                print('start')
                func(*args, **kwargs)
                print('finish')
        return wrapper
    return decorator_repeat

@repeat(3)
def my_func():
    start = 10
    while start >= 0:
        print(f"{start}")
        start -= 1

my_func()