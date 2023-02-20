"""
Minden .py kiterjesztésű file egy modul.
A modulokat tudjuk más fileokban használni, a file-jainkban tárolt változókat, függvényeket
etc. tudjuk használni

Scope és a Namespace

Namespace az egy "mapping" ahhoz, hogy tudd, hogy az adott objectet honnan érsz el

Scope tart az életciklusa és a láthatósága egy objektumnak: változóra vonatkozik

Namespacek: Built-In
            Global
            Enclosing
            Local

"""

# import generator_functions
# from generator_functions import my_gen_

my_val = 10

print(__file__)
print(f"own: {__name__}")

if __name__ == '__main__':
    print("Csak akkor, ha a modul.py-t futtatod közvetlenül")
else:
    print("ha modulként importálod, akkor ez jelenik meg")