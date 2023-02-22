"""
Contextmanager - Kontextusmanager

with open()

Erőforrás management feladatot lát el,
bizonyos feladatokat a felhasználótól függetlenül elvégez
"""

file_path = r"C:\WORK\2023_februar_python\6. alkalom\valami.txt"

with open(file_path, "r", encoding="utf-8") as file_object:
    data = file_object.read()

print(data)