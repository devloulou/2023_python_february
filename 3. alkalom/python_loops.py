"""
Loop - ciklusokkal - iterációk

while - for loop

a while-t akkor használjuk, ha valamilyen event - esemény jellegű - működést szeretnénk
eszközölni

for loop-ot tipikusan arra használunk, hogy végig iteráljunk valamilyen
iterálható objektumon - foreach

while loop:

while feltétel_amíg_igaz:
    kódok_amelyeket_futtatni_kell

"""

a = 5

while a > 0:
    # print(f"{a}")
    # a = a - 1
    a -= 1
game_on = True

cnt = 0
while game_on:
    if cnt == 3:
        game_on = False
    cnt += 1


"""
for loop

for ciklus_valtozo in iterable_object:
    kódok_amelyeket_futtatni_kell

"""
for item in ["Ricsi", "Robi", "Karcsi", "Aranka"][::2]:
    if 1 == 2:
        print(item)

#################################################################

my_list = [1, 2, 3, 4, 5]

# temp = []
# cnt = -1
# for item in my_list:
#     cnt += 1
#     if item%2==0:
#         my_list[cnt] = item*2
#         item = item*2
#         print(item)
#     temp.append(item)
my_list = [1, 2, 3, 4, 5]

for idx, item in enumerate(my_list):
    if item%2==0:
        my_list[idx] = item * 2

my_list = [5, 2, 4, 3, 1]

# nem törlünk elemet abból az iterálható objectből, amin ciklussal iterálunk
temp = []
for idx, item in enumerate(my_list):
    if item%2==0:        
        temp.append(item)

my_list = temp
# print(my_list)

###################################################################

my_dict = {
    "color": "black",
    "brand": {
        "name": "bmw",
        "price": 10_000
    },
    "motor_type": "benzin"
}

for key, value in my_dict.items():
    # if type(value) == dict:
    #     for k, v in value.items():
    #         print(k, v)
        # print(list(value.items()))
    if isinstance(value, dict):
        print(value)

######################################

for item in range(1, 101):
    print(item)

#############################################