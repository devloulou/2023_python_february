"""
JSON

import json

load
loads
dump
dumps

serialization - Python objectből JSONT objectet előállítani
deserialization - JSON stringből Python objectet előállítani
"""
import json

my_dict = {
     "vezetekNev": "Kovács",
     "keresztNev": "János",
     "kor": 30,
     "cim":
            {
                "utcaHazszam": "2. utca 21.",
                "varos": "New York",
                "allam": "NY",
                "iranyitoSzam": "10021"
            },
     "telefonSzam":
            [
                {
                "tipus": "otthoni",
                "szam": "212 555-1234"
                },
                {
                "tipus": "fax",
                "szam": "646 555-4567"
                }
            ]
 }

# print(my_dict)
# JSON kiírás - dump

with open("test.json", "w", encoding="utf-8") as f_obj:
    json.dump(my_dict, f_obj, ensure_ascii=False, indent=4)

with open("test.json", "r", encoding="utf-8") as f_obj:
    data = json.load(f_obj) #deserializáció

print(type(data))

# dumps - JSON stringet hoz létre

data = json.dumps(my_dict, ensure_ascii=False)

print(data)

# loads

my_data = json.loads(data)

print(type(my_data))