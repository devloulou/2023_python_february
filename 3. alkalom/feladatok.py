# adjatok egy tetszőleges kulcs-érték párt a megadott dictionaryhez.
my_dict = {
    "auto": "BWM"
}

my_dict['kulcs'] = "érték"

my_dict.update({"test": "érték"})

# print(my_dict)

# 2. feladat:
# a megadott dictionaryben lévő autokhoz
# adjatok hozzá egy price kulcsot és egy tetszőleges értéket állítsatok be hozzá
my_dict = {
    "auto": [
        {
            "brand": "BMW",
            "color": "white",
            "type": "diesel"
        },
        {
            "brand": "Volvo",
            "color": "yellow",
            "type": "benzin"
        },
        {
            "brand": "Tesla",
            "color": "black",
            "type": "electric"
        }
    ]
}

my_dict['auto'][0]['price'] = 10_000
my_dict['auto'][1]['price'] = 10_000
my_dict['auto'][2]['price'] = 10_000

# print(my_dict)

# 2. feladat:
# az utolsó 2 értéket módosísátok tetszőleges értékre
my_list = ["Ricsi", "Géza", "Karcsi", "Peti"]

my_list[-1] = "r"
my_list[-2] = "t"

# print(my_list)

my_list[-2:] = ["g", "z"]

# print(my_list)
# 3. feladat:
# az alábbi dictionary-ben töröljük a zip_code értékét
my_dict = {
    "shop": {
        "shop_name": "Reál",
        "zip_code": "1111",
        "type": "general store"
    }
}

my_dict['shop']['zip_code'] = None

# my_dict['shop'].pop("zip_code")

del my_dict['shop']['zip_code']

print(my_dict)

