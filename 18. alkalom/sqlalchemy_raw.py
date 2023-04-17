"""
SQLAlchemy

'adatbázis független' - Relációs adatbázis ahhoz tudjuk használni
ha az adatbázisnak van konnectora az SQLAlchemyhez 

3 féleképpen használni:
raw sql-t
expression language
ORM

"""

"""
Raw SQL - stringekként fogjuk az SQL utasításokat megírni a pythonban és 
a libraryvel fogjuk lefuttatni

###############################################################

Általános Data Engineering performancia dolgok:
Backendnek nincs teljes contolrollja a adatbázis felett:.
    - pl. a backend 1 sec alatt 1millió insertet küld a db-nek, az nem jelenti
    azt, hogy 1 sec alatt teljesülni is fog

Az ETL folyamatban, a Load rész leegyszerüsítve az insert utasítások
2 módszer van: recordonként, 1 insert / 1 tranzakció
vagy 'kötelgelve' - batch alapú feldolgozás: x insert / 1 tranzakció

Round Trip: backendről küldöm -> db felé az utasíást -> a db feldolgozza -> és visszaküldi a választ a backendnek

Általánosan igaz az, hogy az ETL folyamatodat tudod gyorsítani azzal, ha 
csökkenteni tudod a round tripek számát.

'kötelgelve' - batch alapú feldolgozás => bulk insert
ha számotokra új libraryvel / új adatbázissal kell dolgoznotok
és a feladat adat integráció, akkor olyan libraryt keressetek
ami tudja ezt a bulk insertes funkciót

sok adat - milliós nagyságrendú rekodszám - integrálása esetén
érdemes közepes batckekben commitálni -> pl. 1000 insertenként 1 commit

minden ETL / ELT folyamat során logolni kell a futási eredményeket / hibákat

"""

from sqlalchemy import create_engine, text, inspect

# engine = create_engine("sqlite:///test.db")
engine = create_engine("postgresql://postgres:postgres@localhost/postgres")

insp = inspect(engine)

# létreehozok 1 sessiont az adatbázis felé
with engine.connect() as conn:
    if not insp.has_table('sql_test'):
        conn.execute(text("create table sql_test(id integer, name text)"))
    for item in range(50):
        # insertnél az a nagy feladat, hogy az értékeket, hogyan adom oda az insert utasításnak
        conn.execute(text(f"insert into sql_test(id, name) values ({item}, 'Ripley')"))
    
    result = conn.execute(text("select name, id from sql_test where id > 30"))

    for item in result:
        print(item)

    conn.commit()
