"""
staticmethod

staticmethodot akkor érdemes haasználni,
ha valamilyen utility funkcionalitást akarok elvégezni

mit nem tud a staticmethod:
nem látja sem az instance sem a class attributumokat -

ha a függvényben nem használunk self-et, akkor az valószínüleg staticmethod

"""


class TestClass:
    temp = 120
    def __init__(self, age):
        self.name = "Karcsi"
        self.age = age

    @staticmethod
    def is_adult(age):
        #True if age > 18 else False -> ternary operátor
        return True if age > 18 else False
    
    def is_adult(self):
        return True if self.age > 18 else False
    

"""
ternary operátor: one liner

igaz feltétel hamis
"""

test = TestClass(40)
print(test.is_adult(test.age))

print(TestClass.is_adult(50))
