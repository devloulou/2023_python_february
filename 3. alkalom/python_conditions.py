"""
Elágazások
if else utasítás

if feltelek_kierteles:
    ha_a_feltetel_teeljesul_akkor_ezen_kodok_fussanak_le
elif feltelek_kierteles:
    ha_a_feltetel_teeljesul_akkor_ezen_kodok_fussanak_le
else:
    ha_a_feltetel_teeljesul_akkor_ezen_kodok_fussanak_le


CPython - interpreter nyelv - C-re fog átfordulni

C-ben:

if (feltetel_ha_igaz){
    itt futnak a kódjaim, ha az if kiértékelése igaz;
}
elif (feltétel) {
    itt is futnak kódok;
}
else {
    else esetén futnak;
}

#################################

indentáció - indentation
default beállítás 4db space vagy 1db tabulator
"""

a = 10

"""
Boolean - True - Igaz
        - False - Hamis

A None - False
"""
# print(a%2==0)

# if a%2==0:
#     print(f"a megadott szám {a} páros")

if a%5==0:
    print(f"{a} nagyobb mint 5")
    print("helllo")
else:
    print("else ágban vagyok")

# if a%5==0: print(f"{a} nagyobb mint 5"); print("Hello")
# else: {print("else ágban vagyok")}


# if a%5==0:
#     {print(f"{a} nagyobb mint 5")}
# else:
#     { print("else ágban vagyok")}

print("************************\n")
a = 21
b = 10

if a > b:
    if a%2==0:
        print(f"a {a} 2.vel oszthatő és nagyobb mint {b}")
    else:
        print(f"{a} nem osztható 2-vel, de nagyobb mint {b}")
else:
    print(f"{a} nem nagyobb mint {b}")
