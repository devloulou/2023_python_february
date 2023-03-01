"""
Feladatok:
1. feladat: Írjatok egy olyan kódot, amely tetszőleges helyre kiír egy file-t, aminek a tartalma
1-100-ig a számok. Minden szám legyen új sorban.
2. feladat: Az 1. feladatban létrehozott file-t olvassátok fel és módosítsátok a tartalmát úgy, hogy
minden 5-el osztható szám legyen csak kiírva új sorban.
3. feladat: A megadott dictionary-ből gyűjtsétek ki az össze kulcsát.
athletics = {
    '100m': {
        'Men': {
            'Gold': 'Marcell Jacobs',
            'Silver': 'Fred Kerley',
            'Bronze': 'Andre De Grasse'
        },
        'Women': {
            'Gold': 'Elaine Thompson-Herah',
            'Silver': 'Shelly-Ann Fraser-Pryce',
            'Bronze': 'Shericka Jackson'
        }
    }
}
4. feladat: Írjatok egy olyan kódot, amely egy magadott mappából csak a csv kiterjesztésű file-okat listázza.
"""

# 1. feladat:
import os

def first_task(file_path):
    temp = [str(item) for item in range(100)]

    writable_str = "\n".join(temp)

    with open(file_path, "w") as f_obj:
        f_obj.write(writable_str)

f_path = os.path.join(os.path.dirname(__file__), "first_tast_1.txt")
# first_task(f_path)

def first_task2(file_path):
    temp = [str(item) for item in range(100)]    

    with open(file_path, "w") as f_obj:
        for item in temp:
            f_obj.write(f"{item}\n")

f_path = os.path.join(os.path.dirname(__file__), "first_tast_2.txt")
# first_task2(f_path)


def first_task3(file_path):
    temp = [f"{str(item)}\n" for item in range(100)]    

    with open(file_path, "w") as f_obj:
        f_obj.writelines(temp)

f_path = os.path.join(os.path.dirname(__file__), "first_tast_3.txt")
# first_task3(f_path)


####################################
# 2. feladat
f_path = os.path.join(os.path.dirname(__file__), "first_tast_3.txt")

def get_data_from_txt(file_path):
    with open(file_path, "r") as f_obj:
        data = f_obj.read()

    return data

def second_task(file_path):
    data = get_data_from_txt(file_path)

    # 1234@1234@1234@123    str.split('@') -> ["1234", "1234", "1234", "123"]
    temp = [item for item in data.split('\n') if len(item) > 0 and int(item)%5==0 ]

    temp = "\n".join(temp)

    with open(file_path, "w") as f_obj:
        f_obj.write(temp)


def second_task2(file_path):
    with open(file_path, "r+") as f_obj:
    # 1234@1234@1234@123    str.split('@') -> ["1234", "1234", "1234", "123"]
        data = f_obj.read()
        temp = [item for item in data.split('\n') if len(item) > 0 and int(item)%5==0 ]
        temp = "\n".join(temp)
        f_obj.seek(0)
        f_obj.write(temp)
        f_obj.truncate()


# second_task2(f_path)

#######################

# 3. feladat
athletics = {
    '100m': {
        'Men': {
            'Gold': 'Marcell Jacobs',
            'Silver': 'Fred Kerley',
            'Bronze': 'Andre De Grasse'
        },
        'Women': {
            'Gold': 'Elaine Thompson-Herah',
            'Silver': 'Shelly-Ann Fraser-Pryce',
            'Bronze': 'Shericka Jackson'
        }
    }
}

def first():
    temp = []
    for k1, v in athletics.items():
        temp.append(k1)
        if isinstance(v, dict):
            for k2, v1 in v.items():
                temp.append(k2)
                if isinstance(v1, dict):
                    for k3,v in athletics[k1][k2].items():
                        temp.append(k3)
    return temp

# print(first())

"""
függvény Rekurzió

rekurzióról beszélünk, amikor egy függvény önmagát meghívja

"""

def my_func():
    print("alma")
    my_func()

# my_func()

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# print(recur_fibo(100))
athletics = {
    '100m': {
        'Men': {
            'Gold': 'Marcell Jacobs',
            'Silver': 'Fred Kerley',
            'Bronze': 'Andre De Grasse'
        },
        'Women': {
            'Gold': 'Elaine Thompson-Herah',
            'Silver': 'Shelly-Ann Fraser-Pryce',
            'Bronze': 'Shericka Jackson'
        }
    }
}
def get_keys(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key)
            yield from get_keys(value)
        else:
            yield (key)

my_list = []

for key in get_keys(athletics):
    my_list.append(key)

# print(my_list)

def get_keys(userDict):
    dict_keys = []
    for k, v in userDict.items():
        dict_keys.append(k)
        if isinstance(v, dict):
            dict_keys.append(get_keys(v))
    return dict_keys


# print(get_keys(athletics))

# keys = []
# def dict_path(path, my_dict):
#     if isinstance(my_dict, dict):
#         for k,v in my_dict.items():
#             if isinstance(v, list):
#                 for i, item in enumerate(v):
#                     if "['" not in path:
#                         keys.append({k: f"['{path}']['{k}'][{str(i)}]"})
#                         dict_path(f"['{path}']['{k}'][{str(i)}]", item)
#                     else:
#                         keys.append({k: f"{path}['{k}'][{str(i)}]"})
#                         dict_path(f"{path}['{k}'][{str(i)}]", item)
#             elif isinstance(v, dict):
#                 keys.append({k: f"{path}['{k}']"})
#                 dict_path(f"{path}['{k}']",v)
#             else:
#                 keys.append({k: f"{path}['{k}']"})

# dict_path("", athletics)

# print(keys)


import os

temp = [item for item in os.listdir(r"C:\WORK\2023_februar_python\6. alkalom") if '.txt' in item]
temp1 = [item for item in os.listdir(r"C:\WORK\2023_februar_python\6. alkalom") if item.endswith(".txt")]
temp2 = [item for item in os.listdir(r"C:\WORK\2023_februar_python\6. alkalom") if item[-4:] == '.txt']

print(temp)
print(temp2)