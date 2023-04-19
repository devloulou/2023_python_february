"""
SQLAlchemy - expression language

szükség lesz egy engine defiícióra

python objektumokat - a librarynek vannak erre a célra elkészített osztályai -
fogunk használni arra, hogy az SQL utasításokat 
elkészítse és lefutassa az adatbázisban
"""

from sqlalchemy import create_engine, text, inspect
from sqlalchemy import MetaData, Table, Column, String, Integer

engine = create_engine("sqlite:///test.db")

"""
Az adatbázis metaadatait - pl. táblákat, azok mezőit és minden, az adatbázihoz tartozó 
információval kapcsolatos objektumot hoz létre
"""
meta = MetaData()

# tábla definíció - adatbázis tábla python oldali reprezentációja
epr_table = Table("expr_table",
                  meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(100))
                  )

epr_table2 = Table("expr_table2",
                  meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(100))
                  )

# epr_table.create(engine)
# epr_table.drop(engine)
meta.create_all(engine)



# insert_statement = epr_table.insert().values(id=1, name='Pisti')
insert_statement = epr_table.insert()
# INSERT INTO expr_table (id, name) VALUES (:id, :name) -> a :id és :name -et bind változónak
# nevezzük: a bind változó futási időben fogja megkapni az értéket
# az sql adatbázisokban van 1 sql motor, ami megtervezi az sql utasítások futtatásának a módját
# a bind változó azt fogja eredményezni, hogy az sql motor nem fog új futási tervet generálni insertenként

dummy_data = [(2, "Ilona"), (3, 'Vica'), (4, 'Piri'), (5, 'Mari'), (6, 'Juli'), (7, 'Gizi')]

# with engine.connect() as conn:
#     #conn.execute(insert_statement)
#     for item in dummy_data:
#         conn.execute(insert_statement.values(id=item[0], name=item[1]))
    
#     conn.commit()

insert_statement = epr_table.insert()
dummy_data = [(2, "Ilona"), (3, 'Vica'), (4, 'Piri'), (5, 'Mari'), (6, 'Juli'), (7, 'Gizi')]

temp = []

for item in dummy_data:
    temp.append(insert_statement.values(id=item[0], name=item[1]))

with engine.connect() as conn:
    for item in temp:
        #conn.execute(item)
        ...
    conn.commit()

#############################################################################
# select
from sqlalchemy import and_, or_
select_statement = epr_table.select()
select_statement = epr_table.select().where(epr_table.c.id < 5)
select_statement = epr_table.select().where(or_(epr_table.c.id < 5, epr_table.c.name == 'Juli'))

delete_statement = epr_table.delete().where(epr_table.c.id > 5)

print(select_statement)
with engine.connect() as conn:

    result_set = conn.execute(select_statement)

    for item in result_set:
        print(item)

delete_statement = epr_table.delete().where(epr_table.c.id > 5)

print(delete_statement)
with engine.connect() as conn:
    conn.execute(delete_statement)
    conn.commit()


update_statement = epr_table.update().where(epr_table.c.id < 5).values(name="Karcsi")

print(update_statement)
with engine.connect() as conn:
    conn.execute(update_statement)
    conn.commit()