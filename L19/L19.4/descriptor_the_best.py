'''
The Best убираем дублирование и используем descriptor
так мы сыэкономили определение класса - пишем дескриптор и он может быть переиспользован множество раз
и всего одна строчка кода в определении класса
'''
# сначала реализуем класс дескриптора
# Дескриптор
class NonNegative:
# в этом классе есть число которое должно быть неотрицательным
    def __init__(self, value = 0):
        self._value = 0
# теперь определяем методы которые говорят нам о том что перед нами descriptor
# это методы __get__ __set__ __delete__
# метод срабатывает по запросу данного атрибута
    def __get__(self, instance, owner):
        return self._value
# метод отвечает за настройку как в  @property
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Отрицательно число! ошибка')
        self._value = value

# Класс
class Order:
    # определяем правила доступа к переменным
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sum(self):
        return self.price * self.quantity

if __name__ == '__main__':
    apple_order = Order('apple', 15, 2)
    print(apple_order.sum())
    # apple_order.price = - 100
    # print(apple_order.sum())
    apple_order.quantity = 5
    print(apple_order.sum())
    apple_order.quantity = -5
    print(apple_order.sum())