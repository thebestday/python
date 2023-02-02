# МЫ ПРИВЫКЛИ ЧТО В ПИТОНЕ МОЖНО ВСЕ ЧТО УГОДНО ПРИСВАИВАТЬ ПОЛУЧАТЬ - но это не совсем так
# и для регулиризации доступа к атрибутам и функциям класса есть такой инструмент как СЛОТЫ
# ДЛЯ ПРИМЕРА РАСМОТРИМ ПУСТОЙ КЛАСС  - не определены параметры: методы и артрибуты
# но нам можно самим присвоить атрибут - например obj.foo = 5
class RegularClass:
    pass
obj = RegularClass()
obj.foo = 5
print(obj.foo, type(obj.foo))
# ЧТО БЫ ЗАПРЕТИТЬ ТАКУЮ ВОЗМЖОЖНОСТЬ (добавлять динамически атрибуты) придуманы были слоты
# СЛОТЫ ЭТО НЕКОТОРЫЙ КОРТЕЖ В КОТОРОМ ОПИСАНЫ ВСЕ ВОЗМОЖНЫЕ методы и атрибуты которые есть у объекта данного класса
# в этом примере задаем класс SlotsClass и в нем задаем кортеж ( в которой одна переменная 'bar')
# создаем объект класса SlotsClass и присваиваем 5-ку атрибуту - КОТОРОГО НЕТ В КОРТЕЖЕ __slots__  - получаем ошибку
class SlotsClass:
    __slots__ = ('bar')
obj = SlotsClass()
obj.foo = 5
print(obj.foo)             # AttributeError: 'SlotsClass' object has no attribute 'foo'