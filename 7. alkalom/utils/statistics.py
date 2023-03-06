"""
statisztikák:
    leghosszab sor - az üres sorok nem számítanak
    állapítsuk meg, hogy hány oldala van: 3000 karakter ~ 1 oldal
    legrövidebb sor - az üres sorok nem számítanak
    leggyakrabban előforduló 5 szó: szónak tekintem azt, ami legalább 5 karakter hosszú
"""
# local import - egy pici sebességet tudsz nyerni
def page_num(data: str) -> int:
    import math
    return math.ceil(len(data)/3000)

def min_max(data: str) -> dict:
    temp = [item for item in data.split('\n') if len(item) > 0]
    # print(max(temp, key=len))
    # print(data.split('\n').index(max(temp, key=len))+1)
    
    # print(sorted(data.split('\n'), key=len, reverse=True)[0])
    min_row = len(temp[0])
    max_row = 0
    min_max_stat = {}
    for item in temp:
        if max_row < len(item):
            min_max_stat['max_row'] = {"value": len(item), "row": item}
            max_row = len(item)
        
        if min_row > len(item):
            min_max_stat['min_row'] = {"value": len(item), "row": item}
            min_row = len(item)
    
    return min_max_stat

def most_common_five_words(data):
    from collections import Counter

    temp = []

    for item in data.split('\n'):
        temp.extend(item.split(' '))

    temp = [item for item in temp if len(item) >= 5]

    c = Counter(temp)
    return c.most_common(5)


if __name__ == '__main__':
    from file_handler import read_data_from_txt
    from params import file_path

    data = read_data_from_txt(file_path)

    pn = page_num(data)
    mn = min_max(data)
    mc = most_common_five_words(data)

    statistics = {
        "page_num": pn,
        "min_max": mn,
        "most_common_words": mc
    }

    print(statistics)