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

        create_statement = "create table {table_name} ("
        for key, val in columns.items():
            create_statement += f"{key} {val}, "

        create_statement = create_statement[:-2] + ')'

        

    def generate_insert_statement(self, data):
        ...
    

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
    folder_path = r"C:\WORK\2023_februar_python\20. alkalom\data"
    test = FileHandler(folder_path)

    file_path = r"C:\WORK\2023_februar_python\20. alkalom\data\circuits.csv"    
    files_list = test.get_files_from_folder()

    for item in files_list:
        file_path = test.folder_path + '/' + item

        data = test.get_data_from_csv(file_path)

        create_statement = test.generate_create_statement(data.dtypes)

        break