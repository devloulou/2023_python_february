"""
String adattípussal

my_str = 'ez egy string'
my_str = "ez másik string"

A String immutable addatípus: megváltoztathatatlan
A string egy iterálható adattípus
a string épíköveit, amelyek a charakterek, nem tudom megváloztatni
"""

my_str = "hello world"
my_str = "Ricsi"

my_str_begin = "sziasztok"
my_str_end = "world"

# stringek összevonását konkatenációnak nevezzük: concatenate strings
my_str = my_str_begin + ' ' + my_str_end 

"""
Slicing művelet: indexek mentén tudunk rész halmazokat, értékeket elérni

 [honnan:meddig:lépték_mértéke]

 [::] = [:]

"""

my_str = "indul a görög aludni"

# print(my_str)
# print(my_str[:10:2])

# print(my_str[4])
# print(my_str[0:5])
# print(my_str[1:10:3])

# print((my_str[-10]))

# print(my_str[0])
# print(my_str[2])

# referencia hivatkozás
my_str = "hello world"
my_str = "szia" + my_str[-6:]
my_str = "szia" + my_str[4:]

alap = "hello world"
kezdet = "szia"

str_v = kezdet + alap[5:]

# print(my_str)
# print(str_v)

######################################################
################ String Formatting ###################

# 1. Old Style formatting: ez már nem elterjedt
# Ricsi vagyok és 32 éves

name = "Ricsi"
age = 32

# %s - placeholder karakter
my_str = "%s vagyok és %f éves" %(name, age)

# 2. "New" Style formatting

name = "Ricsi"
age = 32

my_str = "{name} vagyok és {age:f} éves"

print(my_str.format(name=name, age=age))

# 3. String interpoláció - f' string formázás

name = "Ricsi"
age = 32

my_str = f"{name} vagyok és {age} éves"

print(my_str)

# Template használata
from string import Template

my_template = Template("$name vagyok és $age éves")
print(my_template.substitute(name=name, age=age))

