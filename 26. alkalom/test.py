class First:
    def __init__(self):
        print("first")
        
class Second(First):
    def __init__(self):
        print("second")
    
    def my_func(self):
        print("hello")

class Third(Second, First):
    def __init__(self):
        First.__init__(self)
        print('third')

t = Third()

t.my_func()