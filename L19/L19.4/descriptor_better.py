'''
Better
но есть дублирование кода- каждый (что бы величина > 0 ) мы должны написать property setter
'''
class Order:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = price
        self._quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <0:
            raise ValueError('Цена отрицательная!')

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value <0:
            raise ValueError('Количество отрицательное!')


    def sum(self):
        return self._price * self._quantity

if __name__ == '__main__':
    apple_order = Order('apple', 15, 2)
    print(apple_order.sum())
    # apple_order.price = - 100
    # print(apple_order.sum())        # -200 так быть не должно
    apple_order.quantity = - 1
    print(apple_order.sum())        # -200 так быть не должно

