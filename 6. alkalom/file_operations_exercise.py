
"""
Generáljunk 1000-ig számokat és azokat írjuk ki fileba úgy, 
hogy minden 20. számok után új sorba kerüljenek az adatok

1. szám generálás 1000-ig
2. file művelet


"""
# one liner
def generate_numbers():
    return [i for i in range(1, 1001, 5)]

def write_file():
    with open("file_oper_test.txt", "w") as f_obj:
        cnt = 0
        for idx, item in enumerate(generate_numbers()):
            cnt += 1
            f_obj.write(f"{str(item)}, ")

            if cnt%20 == 0:
                f_obj.write("\n")
            # if idx==19:
            #     f_obj.write("\n")
            # elif idx%20==0 and idx!=0:
            #     f_obj.write("\n")
            # if idx%20==0 and idx!=0:                
            #     f_obj.write("\n")
            # f_obj.writelines(["\n"])


my_list = ["Karics", "Prii\n", "Iza", "5", "István",
"Karics", "Prii\n", "Iza", "5", "István",]

with open("lista_test.txt", "w", encoding="utf-8") as f_obj:
    # f_obj.write(str(my_list))
    f_obj.writelines(my_list)


if __name__ == "__main__":
    write_file()