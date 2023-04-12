"""
Listák
mutable adattípus

hozzá tudunk adni elemet / elemeket
törölni tudunk belőle elemet / elemeket
tudunk módosítani elemeket
tudunk összevonni listákat

my_list = [1, 2, 3, 4, 5, "Ricsi", ("karcsi", 123), print, [1, 2, 3, 4]]

"""

my_list = []

################# elem hozzáadása listához #####################

# 1 elem hozzáadása
name = "Ricsi"
my_list.append("Ricsi")
my_list.append(name)

# több eleme hozzáadása
my_list.extend("Ricsi")
my_list.extend(["Karcsi","bmw", 'pista'])

# megadott helyre történő adatbevitel
my_list.insert(1, "Panka")

################# elem törlése listából #####################

my_list = [50, 60, 50, 80, 90]
# érték alapján törölni
# my_list.remove(20)
my_list.remove(50)

# index mentén törölni
my_num = my_list.pop(1)

# del -es törlés
del my_list[-1], my_list[1]
# del my_list

# print(f"my_num: {my_num}")

my_list = [1, 2, 3, 4, 5]
my_list[-1] = my_list[-1]*10
my_list[-1] = 100
my_list[-1] = (1, 2,)

# my_list[1:4] = "Pisti"
my_list[1:4] = 20, 30

my_list[1:4] = [7, 8, 9]
# my_list[1:4] = [[7, 8, 9]]

# pack - unpack

my_list = [1, 2, 3, 4]

a, b, *c = my_list

# r, t, z = 10, 20, 330

my_list = [1, 2, 3]
my_list2 = [4, 5, 6]

sol2 = []
sol = []
# extend használatával
sol2.extend(my_list)
sol2.extend(my_list2)

# + operator használatával
sol2 = my_list + my_list2

my_list = "Ricsi"

sol = [*my_list, *my_list2]

# print(sol)
####################################################################################

# referencia

a = 10
b = a

b = 20

# print(id(a))
# print(id(b))

# print(a == b)

my_list = [print, "Ricsi", "iskola", 10, 20, ["kutya", "banán"]]

my_list2 = my_list 
my_list3 = my_list2

my_list.append("Karcsi")
# my_list = [2, 3, 4]

my_list2.append('Józsi')

my_list3[0] = 'cica'

# print(f"my_list = {my_list}")
# print(f"my_list2 = {my_list2}")
# print(f"my_list3 = {my_list3}")

# print("-------------")
# print(id(my_list))
# print(id(my_list2))
# print(id(my_list3))

# print(my_list == my_list2 == my_list3)

my_tuple = (1, 2, ["Ricsi", "Pisti"])

my_tuple[-1][0] = "István"


my_list = [1, 2, 3, [4, 5, (print, "Ricsi")]]


my_list[-1].append("valami")

my_list = [1, 2, 3]

my_tuple = (1, 2, 3, my_list)

print(id(my_tuple[0]))
print(id(my_list[0]))
print(id(my_tuple[-1][0]))

# print(my_tuple)



my_dict = {'kulcs': "érték"}
my_dict2 = {"alma": "fa"}

my_dict3 = my_dict | my_dict2

print(my_dict3)



