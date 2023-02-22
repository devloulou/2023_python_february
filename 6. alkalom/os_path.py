import os
import json

# print(__file__)

# print(os.listdir(r"C:\WORK\2023_februar_python\6. alkalom"))

# print(os.path.basename("csoki/pufi/csipsz"))

# print(os.path.exists("csoki/pufi/csipsz"))
# print(os.path.exists(__file__))

# print(os.path.dirname(__file__))
# print(os.path.dirname("csoki/pufi/csipsz"))

alkalom_5 = os.path.dirname(__file__).replace('6. alkalom', '5. alkalom')


alkalom_5 = os.path.dirname(os.path.dirname(__file__)) + "/5. alkalom"

alkalom_5 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "5. alkalom")


print(alkalom_5)

print(os.path.exists(alkalom_5))