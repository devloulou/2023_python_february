"""
Set - halmazok

{1, 2, 3, 4, 5, 5, 5, 5}
duplikáció mentes

Mutable adattípus:  lehet elemet hozzáadni
                    lehet elemet törölni
                    lehet elemet módosítani
"""

my_set = {1, 2, 3}
my_set.add(10)

my_set2 = {4, 5, 6}

my_set.update(my_set2)


my_set = {1, 2, 2, 3}

my_set2 = {4, 5, 6}

my_set.add(10)
# törlés
my_set.pop()
my_set.remove(2)

my_set = {1, 2, 3}

my_set2 = {4, 5, 6, 3, 2, 1}
print(my_set.difference(my_set2))
print(my_set2.difference(my_set))

print(my_set.intersection(my_set2))

print(my_set.issubset(my_set2))