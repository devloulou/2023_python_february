
class Product:
    def __init__(self, price, name):
        self.price = price
        self.name = name

class Milk(Product):
    def __init__(self, price, name):
        self.type = 'milk'
        super().__init__(price, name)

class Meat(Product):
    def __init__(self, price, name):
        self.type = 'meat'
        super().__init__(price, name)


class Cart:
    def __init__(self):
        self.my_cart = {}

    def add_item_to_cart(self, item, cnt):
        ...


class Shop:
    def __init__(self):
        self.warehouse = {}

    def generate_bill(self, cart):
        for item in cart:
            ...

    def add_item_to_warehouse(self, item, cnt):
        if self.warehouse.get(item):
            self.warehouse[item] = self.warehouse[item] + cnt
        else:
            self.warehouse[item] = cnt

    def remove_from_warehouse(self, item, cnt):
        if self.warehouse.get(item):
            if self.warehouse.get(item) >= cnt:
                self.warehouse[item] = self.warehouse[item] - cnt
                return True
            else:
                return Exception(f'Nincs raktáron ennyi árú: {self.warehouse[item]}')
        else:
            return Exception('Nincs ilyen termék')

if __name__ == '__main__':
    test = Shop()

    tej = Milk(3200, )

    test.add_item_to_warehouse()