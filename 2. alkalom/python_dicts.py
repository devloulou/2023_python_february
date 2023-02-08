"""
Dictionary - szótár

a kulcsok minden esetben egyediek 
    -> nem lehet 2 ugyan olyan nevű kulcs egy azonos szinten
{
    "kulcs": "érték",
    "color": "fekete",
    "brand": "BMW",
    "price": 110_000
}

Mutable adattípus: hozzá lehet adni kulcs - érték párt
                   lehet törölni kulcs - érték párt
                   lehet módosítani kulcshoz tartozó értéket
                   lehet összevonni dictionary-ket, 
                    ha és amennyiben a kulcsaik továbbra is egyediek lesznek
"""

my_dict = {
    "brand": "bmw",
    "color": "black",
    "price": 100_000
}

# érték lekérése
# None - pythonban a null érték "üres" érték, semmi

# print(my_dict["brand"])

# print(my_dict.get("pric", "Etele pláza"))

# kulcs - érték hozzáadása

my_dict['brand'] = "volvo"

my_dict['shop'] = "Westend"

my_dict.update({"motor_type":"benzin"})

####################################
# kulcs - értékpár törlése
my_dict = {
    "brand": "bmw",
    "color": "black",
    "price": 100_000
}

value = my_dict.pop("shop", None)

# az utoljára behelyezett kulcs értéket fogja kidobni
value = my_dict.popitem()

del my_dict['color']

# print(value)
# print(my_dict)

####################################################
# érték módosítása

my_dict = {
    "brand": "bmw",
    "color": "black",
    "price": 100_000
}

my_dict['brand'] = "volvo"

my_dict.update({'color': 'yellow'})

# print(my_dict)



my_dict = {
    "brand": "bmw",
    "color": "black",
    "price": 100_000,
    "price": 200_000
}

print(my_dict)


my_dict = {
        "hus": {
            "felvagott": [{
                "szalámi": {
                    "brand": "Hertz",
                    "price": 1000
                },
                "sonka": {
                    "brand": "Pármai",
                    "price": 2000
                }
            }]
        },
        "tej": {
            "zsíros": {
                "laktózos": {
                    "brand": "Riska",
                    "zsírtartalom": 20
                },
                "laktózosmentes": {
                    "brand": "Riska",
                    "zsírtartalom": 10
                }
            }
        }
    }