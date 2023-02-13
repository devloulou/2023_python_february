"""
Comprehension műveletek:

list comprehension
dictionary comprehension
generator expression

my_list = [ciklusváltozó for ciklusvaltozo in iterable_object feltételek(opcionális)]

"""

my_list = [5, 2, 4, 3, 1]
temp = []
for idx, item in enumerate(my_list):
    if item%2==0:        
        temp.append(item)

# list comprehension - gyorsabb, mint for loop-al példányosítani a listát
temp = [item for idx, item in enumerate(my_list) if item%2==0]

# dictionary comprehension

my_dict = {}

for idx, item in enumerate(range(1, 10)):
    my_dict[idx] = item

my_dict = { idx:item for idx, item in enumerate(range(1, 10))}



# print(my_dict)

import sys

temp = [item for item in range(1, 100)]

# generator object - generator expression
my_gen = (item for item in range(1, 100))


# print(sys.getsizeof(temp))
# print(sys.getsizeof(my_gen))
"""
Generator object egy iterable object
Generator expression
lazy evaluation-t használ -> nem értékeli ki a kifejezést futási időben 
                          -> az elemeket nem értékeli ki, 
                             nem foglal nekik memória területet


"""

temp = [item for item in range(1, 1000)]

# generator object - generator expression
my_gen = (item for item in range(1, 1000))

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

for item in my_gen:
    print(item)