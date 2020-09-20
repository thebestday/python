# посмотрим на практике - пишем класс и в ините зададим какой-нибудь параметр
import sys

class Someclass:
    def __init__(self):
        self.my_attr = 1

# создадим класс уже со слотами
class SomeclassWithSlots:
    # что бы воспользоваться этим механизмом необходимо определить магический атрибут __slots__, который позволяет задать ограниченный набор атрибутов, которыми будет обладать экземпляр класса.  - кортеж с переменными
    __slots__ = ('my_attr', 'only_my_attr')
    # второму атрибуту не будем присваивать значение в ините - оставим неопределенным в самом классе
    def __init__(self):
        self.my_attr = 1

# делаем точку входа
if __name__ == '__main__':
    # # создаем объект данного класса
    # obj = Someclass()
    # # порядок доступа к атрибуту совершенно обычный
    # print(obj.my_attr)
    # # динамически создадим новый отрибут
    # obj.not_my_attr = -1
    # print(obj.not_my_attr)
    # # проверим что в списке новых атрибутов появился новый атрибут с помощью функции dir
    # print(dir(obj))              #  [....'__dict__'.... 'my_attr', 'not_my_attr']
    # # метод  '__dict__' может показать значения и названия всех атрибутов которые есть у данного объекта
    # print(obj.__dict__)
    # # можно пользоваться этим словарем(но очень редко) по ключу можем получить значения
    # print(obj.__dict__['my_attr'], obj.__dict__['not_my_attr'])
    # создадим объект нового класса
    obj_slots = SomeclassWithSlots()
    # и попробуем сделать присвоение атрибуту (не указанному в слоте)  и получаем ошибку AttributeError: 'SomeclassWithSlots' object has no attribute 'not_my_attr' - данный класс не содержит такого атрибута
    # obj_slots.not_my_attr = -1
    # print(obj_slots.not_my_attr)    # AttributeError: 'SomeclassWithSlots' object has no attribute 'not_my_attr'
    # если присвоим второму - пустому атрибуту то все работает
    obj_slots.only_my_attr = -1
    print(obj_slots.only_my_attr)
    # мы можем определить этот атрибут  как фунцию лямбда
    obj_slots.only_my_attr = lambda x: x**2
    print(obj_slots.only_my_attr)       # <function <lambda> at 0x7f8855fc6310>
    # и можем теперь спокойно использовать данную функцию -(т.е атрибуты прописанные в слоте это по сути имена -а что под ними скрывается решает разработчик класса)
    print(obj_slots.only_my_attr(8))
    # но сейчас у данного объекта obj_slots не должно быть метода  '__dict__'
    # print(obj_slots.__dict__)         # AttributeError: 'SomeclassWithSlots' object has no attribute '__dict__'
    print(dir(obj_slots))   # видим что нет метода  '__dict__'

    print(sys.getsizeof(SomeclassWithSlots))
    print(sys.getsizeof(Someclass))


# слоты это хорошая практика
# использование слотов это такая закрытая инкапсуляция - т.е если данный класс законченный то и не нужно его трогать
# объект класса занимает меньше места -меньеш оперативной памяти
# ограничение доступа - нет лишних прав(доступа) на атрибуты класса
