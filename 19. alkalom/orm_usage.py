"""
ORM - Object Relational Mapping

adatbázis tábla python oldali reprezentációja
mi fogjuk definiálni a táblához tartozó osztályt


2 csoportra lehet osztani a világon fellelhető libraryket
1. open source
2. third party cég által fejleszett megoldás

"""

from sqlalchemy import create_engine, update, delete, select
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///test.db")

base = declarative_base()

# a tábla definíciókat model-nek nevezzük
class FilmTable(base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    director = Column(String)

Session = sessionmaker(engine)
session = Session()

base.metadata.drop_all(engine)
base.metadata.create_all(engine)

####################################################
# insert 
alien = FilmTable(id=1, title='Alien', director="Ridley Scott")
starwars = FilmTable(id=2, title='Star Wars', director="George Lucas")

# bulk insert
session.add_all([alien, starwars])
session.commit()

#####################################################
# select

movies = session.execute(select(FilmTable).where(FilmTable.id == 1))

for i in movies:
    print(i[0].title)
    print(i[0].id)
    print(i[0].director)

movies = session.query(FilmTable).filter(FilmTable.id==2)
# movies = session.query(FilmTable).group_by(FilmTable.id)#.filter(FilmTable.id==2)

# for movie in movies:
#     print(movie.director)
#     print(movie.id)
#     print(movie.title)

"""
Serialization - Python objectből adatbázis record-ot készít
Deserialization - adatbázis recordból Python objectet
A python object ebben az esetben a definiált ORM model lesz

"""

##########################################################
# update

for movie in movies:
    movie.title = "Star Wars: New Hope"
    session.commit()


session.execute(update(FilmTable)
    .where(FilmTable.id == 1)
    .values(title="Alien: A nyolcadik utas a halál"))

session.commit()

################################
#delete

test = session.query(FilmTable).filter(FilmTable.id == 2).delete()
# delete from movies where id in (select id from movies where id = 2)
session.commit()

test = session.execute(delete(FilmTable).where(FilmTable.id == 1))
# delete from movies where id = 1
print(delete(FilmTable).where(FilmTable.id == 1))
session.commit()

"""
Következő órán:

dunderscore methods
egy feladatot, ami ORM-el fogunk megvalósítani
git
"""