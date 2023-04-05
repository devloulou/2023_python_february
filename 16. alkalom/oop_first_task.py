"""
Szimuláljuk le egy önkiszolgáló kassza működését

vannak termékek, amelyeket megveszek pénzért, 
ezeknek a terméknek van értéke
és a kassza összeadja a vásárolt termékeim árát
és generál nekem egy számlát

3 terméket
tej
kenyér
felvágott

Vásárláskezelő
ami megkap egy valamilyen iterálható formában a termékeket amiket venni akarok
és összeállít egy blokkot
legyen a nettó - bruttó
"""

from typing import List

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price


class Cassier:
    def manage_products(self, products: List[Product]):
        final_price = 0
        bill = []
        final_bill = {'final_price': 0,
                      'products': bill}
        for item in products:
            final_price += (item['product'].price * item['cnt'])
            bill.append({'product_name': item['product'].product_name ,
                         'cnt': item['cnt'],
                         'price_cnt': item['product'].price,
                         'price_full': item['product'].price * item['cnt']})

        final_bill['final_price'] = final_price
        return final_bill

if __name__ == '__main__':
    k = Cassier()

    bread = Product('white', 1000)
    milk = Product('UHT 2.5', 800)
    meat = Product('Pick salami', 5000)

    basket = [{bread: 5}, {milk: 3}, {meat: 4}]
    basket = [{'product': bread, 'cnt': 5},
              {'product': milk, 'cnt': 3},
              {'product': meat, 'cnt': 4}]

    bill = k.manage_products(basket)

    print(bill)
    # for inner_dict in basket:
    #     product = list(inner_dict.keys())[0]
        
    #     final_price += (inner_dict[product]*product.price)

    # for item in basket:
    #     final_price += (item['product'].price * item['cnt'])


    # print(final_price)