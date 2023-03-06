import os
from utils.file_handler import read_data_from_txt, write_json
from utils.statistics import page_num, min_max, most_common_five_words
from utils.params import file_path, statistics_folder


# read_data_from_txt("teszt")

def generate_statistics():
    data = read_data_from_txt(file_path)

    pn = page_num(data)
    mn = min_max(data)
    mc = most_common_five_words(data)

    statistics = {
        "page_num": pn,
        "min_max": mn,
        "most_common_words": mc
    }

    json_path = os.path.join(statistics_folder, 'statistics.json')
    write_json(json_path, statistics)

if __name__ == '__main__':
     generate_statistics()


