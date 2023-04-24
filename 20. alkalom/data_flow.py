"""
Feladat:
a data mappában lévő csv-ket kellene adatbázisba betölteni
az adatbázis táblát automatikusan generálva hozzuk létre
és utána töltsük be az adatokat az adatbázisba

fogunk írni riportokat olyan adatseten, amit nem ismerünk
A megvalósítást modulárisan kell megoldani

A megoldáshoz vezető út:
1. kiolasni a csv-k tartalmát
    file olvasás - pandas
    végig iterálni a könyvtáron, megvizsgálni, hogy csak csv-legyen

2. létre kell hozni a táblákat
    adatbázis táblát automatikusan generálva hozzuk létre
    dataframe-nőél olvassuk ki a mező neveket és azt használjuk az sql create-hez
    A VALÓ ÉLETBEN NEM íGY DOLGOZUNK, ABBAN AZ ESETBEN, HA FOLYAMATOS ADATINTEGRÁCIÓT CSINÁLUNK

3. Adatbetöltés megvalósítésa
    insertek - 
    az insert utasítást legenerálni
    leffutatni az inserteket



"""