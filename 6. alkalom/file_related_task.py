"""
File műveletek

txt, JSON, csv, xls

3 lépés a file műveletek esetében:
1. megnyitni a file-t valamilyen megnyitási móddal
2. itt történik a fileművelet:
    - olvasás
    - írás
3. ha befejeztük a file műveleteket, akkor be kell zárni a file-t

Törlést azt nem a fenti megállapításhoz soroljuk


"""
# file műveletnél szükségem van az eléri útvonalra, javaslat:
# használjatok teljes eléri útvonalat
file_path = r"C:\WORK\2023_februar_python\6. alkalom\valami.txt"
f = open(file_path, "r", encoding="utf-8")
data = f.read()
f.close()

test_text = "élhjaráélhjarepiohjeaprohaerpohear\n aídsfélkíjsyédhgyí\n élsdhíh\n"

f = open("file_write_test.txt", "w", encoding="utf-8")
f.write(test_text)
f.close()