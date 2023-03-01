import os
import json

# import probléma
# if __name__ == '__main__':
#     from params import file_path
# else:
#     from utils.params import file_path

# import probléma
# import sys
# print(sys.path)
# sys.path.append(r"C:\WORK\2023_februar_python\7. alkalom")

"""
A függvény prototipizálás

"""
def read_data_from_txt(f_path):
    """
    This function needs to read data from txt
    """
    # le kell védenünk azt az esetet, hogy mi történjen,
    # ha nem létezik a megadott file útvonal
    if not os.path.exists(f_path):
        raise Exception(f"The given file {f_path} is not exists")
        raise FileNotFoundError(f"The given file {f_path} is not exists")
    
    if not os.path.isfile(f_path):
        raise Exception(f"The given path {f_path} is not a file")

    with open(f_path, "r", encoding="utf-8") as f_obj:
        data = f_obj.read()
       
    return data

# type hint
def write_json(json_path: str, data: dict = {}) -> None:
    # if not os.path.exists(os.path.dirname(os.path.dirname(json_path))):
    if not data:
        raise ValueError(f"Given data {data} is empty")
    with open(json_path, "w", encoding="utf-8") as f_obj:
        json.dump(data, f_obj, ensure_ascii=False, indent=4)

    return True


if __name__ == '__main__':
    from params import file_path
    test_path = r"C:\WORK\2023_februar_python\7. alkalom"
    data = read_data_from_txt(file_path)

    write_json("test")