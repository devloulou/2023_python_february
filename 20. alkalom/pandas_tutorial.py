"""
Pandas - data library
mindenféle adat feldolgozással kapcsolatos feladatra 
viszonylag jól kezeli a nagy fileokat

file típustóül függetlenül ugyan abban a struktúrában nyitja meg a filet

3 object típus:
Series: mint egy oszlop az excelben: van adattípusa, van az oszlopnak neve,
lehet az oszlopnak indexe, oszlopos elrendezésben van az adat

DataFrame: mint egy adatbázis tábla -> oszlopokból áll (Series), oszlopoknak van adattípusa
lehet indexe

Panel - nem fogunk beszélni -> multi dimenzionális "tömb"

"""
################Series###################

import pandas as pd

my_list = [item for item in range(10, 16)]

s = pd.Series(data=my_list)

s.index = ['Tojás', 'Kenyér', 'Tej', 'Felvágott', 'Pékárú', 'Rudi']


my_dict = {'day1': 420, 'day2': None, "day3": 390}

s = pd.Series(data=my_dict)


s.fillna(s.median(), inplace=True)
# s = s.fillna(s.median())

# print(s)
# print(s.median())

###################DataFrame####################

"""

pandas.DataFrame(data, index, columns, dtype, copy)

"""

data = {
    "calories": [430, 530, 1240],
    "duration": [120, 200, 400]
}

df = pd.DataFrame(data)


# print(df.head(2))

# print(list(df.columns))
# print(df.dtypes)


file_path = r"C:\WORK\2023_februar_python\20. alkalom\data\circuits.csv"

df = pd.read_csv(file_path, sep=',')

# print(df.columns)
# print(df.dtypes)

print(df.to_dict(orient="records"))