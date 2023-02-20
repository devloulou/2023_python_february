"""
Generator függvények

nem return-öl, hanem yield-el
a generator függvény is lazy evaluationt használ

meg tudod állítani a függvény futását és vissza tudsz térni a megállított
"pillatnathoz"

"""
# ez egy generator compregension
my_gen_ = (item for item in range(100))

def my_func():
    return 1
    return 2
    return 3

# print(my_func())

def my_gen():
    print("yield 1 előtt")
    yield "almafa"
    print("első yield után")
    yield "cseresznyefa"
    print("masodik yield után")
    yield 10

func = my_gen()
# print(next(func))
# print(next(func))
# print(next(func))

# for item in func:
#     print(item)

print(f"modul: {__name__}")