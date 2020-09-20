"""
descriptor ДЕСКРИПТОР это атрибут объекта который связан с его поведением
фактически descriptor является инкапсулированием протокола взаимодействия с атрибутом
соединение descriptor-ра с классом protocol __get__ __set__ __delete__
descriptor определяет как формируется доступ к кому-то атрубуту или ф-и
descriptor он формально в коде выглядит как класс у которого опеределены методы __get__ __set__ __delete__
через эти методы происходит настройка доступа к атрибуту или ф-и (метода класса)
мы уже сталкивались с дескриптором при создании класса в sqlalchemy
from sqlalchemy import Column,Integer,String

class User(Base):
    id = Column(Integer, primary_key = True)
    name = Column(String)
возникает вопрос почему id у нас не находиться в привычном __init__ в инициализациоонй функции
и почему он определяется через какой-то Column - что такое Column ??? Column и есть дескриптор
он определяет доступ и формат записи в эти переменные  id name
Column является дескриптором с некоторыми параметра
"""


"""
Bad example Создадим класc в котором доступ не определен (так обычно не делают)
"""
class Order:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sum(self):
        return self.price * self.quantity

if __name__ == '__main__':
# сразу несколько проблем - главная то что имеем полный доступ а артибутам и может записывать в них то что не соответсвует действительнссти
    apple_order = Order('apple', 15, 2)
    print(apple_order.sum())
# можем записать такой код -но так быть не должно - мы должны контролировать запись в price .... и мы может это делать с помощтью настройки свойств
    apple_order.price = - 100
    print(apple_order.sum())        # -200 так быть не должно


