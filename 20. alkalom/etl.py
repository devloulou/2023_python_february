import time

# from utils.file_handler import FileHandler
# from utils.database_handler import DatabaseHandler
# from utils.parameters import url

from utils import url, FileHandler, DatabaseHandler
from utils.parameters import folder_path

print(folder_path)

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(time.time() - start_time)
        return result
    return wrapper


@timeit
def run_etl():
    folder_path = r"C:\WORK\2023_februar_python\20. alkalom\data"
    test = FileHandler(folder_path)
    sql = DatabaseHandler(url)

    file_path = r"C:\WORK\2023_februar_python\20. alkalom\data\circuits.csv"    
    files_list = test.get_files_from_folder()

    for item in files_list:
        file_path = test.folder_path + '/' + item
        table_name = item[:-4]

        data = test.get_data_from_csv(file_path)

        create_statement = test.generate_create_statement(data.dtypes).format(table_name=table_name)

        insert = test.generate_insert_statement(data.dtypes).format(table_name=table_name)

        sql.run_query(f"drop table {table_name};")

        sql.run_query(create_statement)

        sql.insert_data(insert, data)

        print(f"{table_name} loaded success")

@timeit
def run_etl_not_bulk():
    folder_path = r"C:\WORK\2023_februar_python\20. alkalom\data"
    test = FileHandler(folder_path)
    sql = DatabaseHandler(url)

    file_path = r"C:\WORK\2023_februar_python\20. alkalom\data\circuits.csv"    
    files_list = test.get_files_from_folder()

    for item in files_list:
        file_path = test.folder_path + '/' + item
        table_name = item[:-4]

        data = test.get_data_from_csv(file_path)

        create_statement = test.generate_create_statement(data.dtypes).format(table_name=table_name)

        insert = test.generate_insert_statement(data.dtypes).format(table_name=table_name)

        sql.run_query(f"drop table {table_name};")

        sql.run_query(create_statement)

        sql.insert_data_not_bulk(insert, data)

        print(f"{table_name} loaded success")

if __name__ == '__main__':
    run_etl()
    print("----------------------------------------")
    # run_etl_not_bulk()
