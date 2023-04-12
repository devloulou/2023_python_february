"""
'private' változók kezelése Pythonban

getter, setter, deleter - 

attributum: változókra gondolok

getter - lekérdezhető legyen a private attributume értéke
setter - új érték hozzárendelése a private attributumhoz
deleter - az értéket - és magát a változót - fogja megszűntetni

"""

class TestClass:
    def __init__(self):
        self.__value = 100

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value

    def del_value(self):
        """
        del működése: 
        """
        del self.__value
    
    # sofistikáltabb getter - setter
    # property()

    def __get_value(self):
        return self.__value
    
    def __set_value(self, value):
        self.__value = value

    def __del_value(self):
        """
        del működése: 
        """
        del self.__value

    value = property(__get_value, __set_value, __del_value)

class TestClass:
    def __init__(self):
        self.__value = 100
        self.__name = "Ricsi"
        self.__age = 32

    @property
    def value(self):
        ...
    
    @value.getter
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @value.deleter
    def value(self):
        del self.__value

if __name__ == '__main__':
    test = TestClass()

    test.value = 500
    # del test.value
    print(test.value)

    # # test.set_value(5500)
    # test.del_value()
    # print(test.get_value())