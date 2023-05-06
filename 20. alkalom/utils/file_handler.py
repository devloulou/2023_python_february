import os
import pandas as pd


class FileHandler:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_data_from_csv(self, csv_path):
        """This open a csv and give a DataFrame back"""
        return pd.read_csv(csv_path, sep=',')
    
    def get_files_from_folder(self):
        return os.listdir(self.folder_path)
    
    
    def generate_create_statement(self, data):
        columns = self.generate_dtypes_mapping(data)

        create_statement = "create table if not exists {table_name}("
        for key, val in columns.items():
            create_statement += f"{key} {val}, "

        create_statement = create_statement[:-2] + ')'

        return create_statement

    def generate_insert_statement(self, data: pd.Series):
        """
        Az előző feladata alapján felhasználtam a teljes kódot annyi különbséggel,
        hogy csak a key-t adtam hozzá az insert_statement-hez
        """
        columns = self.generate_dtypes_mapping(data)
        insert_statement = "insert into {table_name} ("
        insert_values = " values ("
        for key, val in columns.items():
            insert_statement += f"{key}, "
            insert_values += f":{key}, "

        """
        insert generálásnál a values résznél bind változókat célszerű használni
        """
        # insert_statement = insert_statement[:-2] + ')' + insert_values[:-2] + ')'
        insert_statement = f"{insert_statement[0:-2]}){insert_values[0:-2]})"

        # inserted_values = insert_data.values
        # value_statement = "values ("
        # to_db = ""
        # list_of_inserted_data = []

            

        # for idx in range(len(inserted_values)):
        #     to_db = ""
        #     print(inserted_values[idx])
        #     for inx in range(len(inserted_values[idx])):
        #         to_db += str(inserted_values[idx][inx]) + ", "
        #     full_value = value_statement + to_db[:-2] + ")"
        #     """insert_to_db - ebben van az összesített adat, amit adatbázisba lehetne küldeni"""
        #     insert_to_db = insert_statement + " " + full_value
        #     """vagy listában tárolni"""
        #     list_of_inserted_data.append(insert_to_db)

        return insert_statement
    

    def generate_dtypes_mapping(self, data: pd.Series):
        cols = data.to_dict()
        columns = {}
        for key, value in cols.items():
            d_type = None

            if value == 'object':
                d_type = "text"

            if value == 'int64':
                d_type = 'integer'
            
            if value == 'float64':
                d_type = "decimal"

            columns[key] = d_type

        return columns

if __name__ == '__main__':
    from database_handler import DatabaseHandler
    from parameters import url

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

        sql.run_query(create_statement)

        sql.insert_data(insert, data)

        print(f"{table_name} loaded success")
