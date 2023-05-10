from sqlalchemy import create_engine, text
import pandas as pd

class DatabaseHandler:
    def __init__(self, url):
        self.engine = create_engine(url)

    def run_query(self, query):
        with self.engine.connect() as conn:
            try:
                conn.execute(text(query))
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(str(e))


    def insert_data(self, query, data: pd.DataFrame):
        with self.engine.connect() as conn:
            try:
                # bulk insert funkció
                conn.execute(text(query), data.to_dict(orient="records"))
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(str(e))

    def insert_data_not_bulk(self, query, data: pd.DataFrame):
        with self.engine.connect() as conn:
            try:
                """
                a python elküldi > db-nek az insertet -> lefut az insert ->visszaküldi a választ a db
                ez a folyamat egy round trip
                """
                for item in data.to_dict(orient="records"):
                    conn.execute(text(query), item)
                    conn.commit()
            except Exception as e:
                conn.rollback()
                print(str(e))
    
    
if __name__ == '__main__':
    url = "postgresql://postgres:postgres@localhost:5432/postgres"
    test = DatabaseHandler(url)

    test.run_query('create table python_test(name text)')