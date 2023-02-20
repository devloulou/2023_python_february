# 1. feladat: írjatok egy olyan megoldást, amely a lenn megadott listából
# minden 2. elemet kitörli

my_list = ['alma', 'körte', 'barack', 'bizili', "banán", "narancs"]

my_new_list = my_list[::2]
# print(my_new_list)

temp = []
for idx, item in enumerate(my_list):
    if idx%2==0:
        temp.append(item)

my_list = temp

# print(my_list)

# 2. feladat: A megadott listából töröljétek minden 3-al osztható számot

my_list = [item for item in range(100)]

temp = []
for item in my_list:
    if item%3==0:
        temp.append(item)

# print(temp)

# 3. feladat: a my_dict-et töltsétek fel elemekkel az elvárt eredménynek megfelelően.
# elvárt eredmény: {0:1, 1:2, 2:3, 3:4 ... 9:10}
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_dict = {}

# for idx, item in enumerate(my_list):
#     my_dict[idx] = item

# for item in my_list:
#     my_dict[item-1] = item

# for item in range(len(my_list)):
#     my_dict[item] = item + 1

my_dict = {idx:item for idx, item in enumerate(my_list)}
# print(my_dict)

# feladat:
# adjatok egy tetszőleges kulcs-érték párt a megadott dictionaryhez.

my_dict = {
    "auto": "BWM"
}

my_dict['kulcs'] = "érték"

my_dict.update({'kulcs': "érték"})

#################################################################################
# feladat:
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

for item in my_dict['auto']:
    item['price'] = 10_000

# print(my_dict)
#############################################################

def addKeyAndValue(dict, keyUpdate, value):
    for i in range(len(dict["auto"])):
        dict["auto"][i].update({keyUpdate: (i+1)*value})
    return dict


# print(addKeyAndValue(my_dict, "price", 10000))

##############################################################

#Nem szeretjük a francia autót, töröljök a renault az autók közül. A többi érték ne változzon.

my_dict = {
            "auto": [{"type": "Volvo",
                     "color": "gold"
                    },
                    {"type": "Audi",
                     "color": "red"
                    },
                    {"type": "Reanult",
                     "color": "White"
                    } ],
            "driver": ["Heikki Kovalainen", "Bruno Senna", "Sebastien Buemi"],
            "licence": False,
            "age": 18
        }
###################################################

my_list2=[]
searchedText = "Reanult"

# for key, value in my_dict.items():
#     if type(value) != list:
#         continue

#     for idx, listItem in enumerate(value):
#         if type(listItem) == dict:
#             for key2, value2 in listItem.items():
#                 if value2 == searchedText:
#                     del my_dict[key][idx]

#         if type(listItem) == list:
#             ...

# print(my_dict)

# for idx, item in enumerate(my_dict['auto']):
#     for k, v in item.items():
#         if v == 'Reanult':
#             my_dict['auto'].pop(idx)
#             # ide kell rakni a törlést


for item in my_dict["auto"]:
    if item["type"] == "Reanult":
        my_dict["auto"].remove(item)

# print(my_dict)

# töröljétek ki azt az elemet, ahol nem szerepel író

my_dict = {
    "books": [
        {
            "writer": "J.K. Rowlings",
            "book": "Harry Potter and the Goblet of the Fire"
        },
        {            
            "book": "Sorstalanság"
        },
        {
            "writer": "Mikszáth Kálmán",
            "book": "Szent Péter esernyője"
        },
        {            
            "book": "Sorstalanság",
            "writer": ""
        }
    ]

}

def deleteWriter(dict, delType):
    for i, item in enumerate(dict["books"]):
        # if not item.get(delType) or item.get(delType) == "":
        if item.get(delType) == None or item.get(delType) == "":
            dict["books"].pop(i)
    return dict


# print(deleteWriter(my_dict, "writer"))


# töröljétek az összes olyan elemet a listából, amely
# nem osztható maradék nélkül 3-al



my_list = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

temp = []
for item in my_list:
    if item%3!=0:
        temp.append(item)

my_list = [item for item in my_list if item not in temp]

# print(my_list)


# 5. feladat:
# írjatok egy olyan programot, amely a 2 listából csinál egy dictionary-t
# pl: {
#   1: "alma",
#   2: "körte"
#   .
#   .
#   5: "dinnye"
# }
my_dict = {}
my_list = [1, 2, 3, "Józsi", 5]
my_list2 = ["alma", "körte", "barack", "banán", "kivi"]

for idx, item in enumerate(my_list):
    my_dict.update({item:my_list2[idx]})


my_dict = dict(zip(my_list, my_list2))

# print(dict(my_dict))
#Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a
# legkisebb értéket ezek közül!

def my_min(a, b, c):
    if a < b and a < c:
        return a
    if b < a and b < c:
        return b
    if c < b and c < a:
        return c

def my_min(*args):
    return min(args)

# print(my_min(2, 2, 33))

#Írj egy Python programot, amely bekér egy dolgozat pontszámot (x) a felhasználótól és kiír egy
# érdemjegyet az alábbiak szerint! 1: ; 2: 50<=x<60; 
# 3: 60<=x<70; 4: 70<=x<85; 5: x>=85.

def my_func(x):
    if x < 50:
        return 1    
    if x < 60:
        return 2
    if x < 70:
        return 3
    if x < 80:
        return 4
    else:
        return 5


print(my_func(49))