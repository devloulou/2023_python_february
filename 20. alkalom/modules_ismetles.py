"""
Minden .py kiterjesztésű python file egy modul

A package egy mappa, amelyben több modul van.
python számára az tekinthető teljes mértékbe package-nek, amiben
van egy __init__.py file

Minden .py file egy objektum.
Amikor létrehozunk egy .py file-t, és futtatjuk, 
akkor bizonyos változók tartoznak a fileokhoz és ezek értéket kapnak.

Minden filenak, amit futtatok a __name__ változó a __main__ értéket fogja kapni
"""

print(__name__)