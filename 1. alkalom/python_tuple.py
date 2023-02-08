"""
Összetett adattípusok - Tuple

A tuple egy immutable adattípus és iterálható adattípus - iterable object

my_tuple = (10, "Ricsi", 123, 4324, "Karcsi")

rajta is működik a  slicing

immutable: nem tudok hozzáadni elemet,
           nem tudok törölni elemet,
           nem tudok megváltozatatni elemet

ezek miatt biztonságos
"""

my_tuple = (1, 2, 3, 4, 5)
my_tuple = my_tuple[0:-1]

my_tuple = (1, 1, 2, 3, 4, 10)

print(my_tuple.count(1))
print(my_tuple.index(1))

print(my_tuple)


"""
A következő alkalommal:
listák, dictionaryk, set, elágazások, indentációt,
ciklusok
"""