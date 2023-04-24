from sqlalchemy import create_engine, text

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

    
    
if __name__ == '__main__':
    url = "postgresql://postgres:postgres@localhost/postgres"
    test = DatabaseHandler(url)

    test.run_query('create table python_test(name text)')