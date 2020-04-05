from math import hypot
class Point2D():

    def __init__(self, x,y):            # координаты точки на вход
        self.coord = [x,y]              # print(point1)  вернет указатель на объект <__main__.Point2D object at 0x7f0c789dceb8>

    def __str__(self):        # что бы вывод был грамотным - делаем маг.метод __str__ который применятеся при print()
        # возвращаем строку которую хотим напечатать принтом в коде
        return f'Point: ({self.coord[0]}, {self.coord[1]})'  #   print(point1)    Point: (1, 1)

    def __del__(self):                    # очистить память от нашего объекта
        #  используем обычный оператор del для удаления атрибутов объекта
        del self.coord     # del point1  удалали  print(point1)   NameError: name 'point1' is not defined

    # удобно чтобы ф-я len применялась бы к каждому объекту некоторго списка(он может состоять из разных объектов)
    # для этого доопределим в классе реакцию на фун-ю  len
    # print(len(point1)) без доопределения класса выдает ошибку   TypeError: object of type 'Point2D' has no len()
    # def __len__(self):
    #     # вернем длину вектора - расстояние от точки до нуля
    #     return (self.coord[0]**2 + self.coord[1]**2)**0.5

    #аналог - метод объекта возращает дистанцию - вернем длину вектора - расстояние от точки до нуля
    def distance(self):
        return (self.coord[0]**2 + self.coord[1]**2)**0.5

    # итерация по объектам которые лежат в листе - что бы работал метод in
    # атрибут должен быть итерируемый - напрмер лист из координат
    def __getitem__(self, item):
        return self.coord[item]

    # Операция сравнения работает т.к операция сравнения наследуется из общего для всех класса - классс objects
    # равенство будет тогода когда объекты равны целиком т.е print(point1==point1)  # True только в этом случае
    # РАВЕНСТВО ЕСЛИ НЕ УКАЗАНО ЯВНО  - происходит сравнение ПОНОСТЬЮ (как объекты)
    # перегрузка равенства дает возможность сравнивать объекты other - это второй объект сравнения
    def __eq__(self, other):
        # можно сравнить точки поокоординатно
        # return (self.coord[0] == other.coord[0])&(self.coord[1] == other.coord[1])
        return self.coord == other.coord         # так тоже можно

    #------------------------------------------------
    # TypeError: '<' not supported between instances of 'Point2D' and 'Point2D'
    # ЛОГИЧЕСКАЯ ОПЕРАЦИЯ НЕ ПОДДЕРЖИВАЕТСЯ  print(point1 < point2)
    d = 1.4142135623730951 # удобно сравнивать если в другом классе есть тоже d но с другим значением
    # def __lt__(self, other):
    #     return (self.d < other.d )
    #
    def __lt__(self, other):
        return self.distance() < other.distance()
    #--------------------------------------------------

    # TypeError: '<=' not supported between instances of 'Point2D' and 'Point2D'
    # перегрзука меньше равно  le от англ. «less equal» — «меньше равно»
    def __le__(self, other):
        return (self.distance() <= other.distance())

    # TypeError: '>=' not supported between instances of 'Point2D' and 'Point2D'
    # ge от англ. «greater equal» — «больше равно»
    # перегрузка больше равно
    def __ge__(self, other):
        return (self.distance() >= other.distance())

    # TypeError: '>' not supported between instances of 'Point2D' and 'Point2D'
    # gt от англ. «greater than» — «больше чем»
    # перегрзука больше
    def __gt__(self, other):
        return (self.distance() > other.distance())

    # TypeError: unsupported operand type(s) for +: 'Point2D' and 'Point2D'
    # перегрузка сложения метод __add__ возвращает объект этого же класса
    def __add__(self, other):
        return Point2D(self.coord[0] + other.coord[0], self.coord[1] + other.coord[1])

    # TypeError: unsupported operand type(s) for *: 'Point2D' and 'Point2D'
    # перегрзука умножения
    def __mul__(self, other):
        return Point2D(self.coord[0] * other.coord[0], self.coord[1] * other.coord[1])

    #TypeError: bad operand type for abs(): 'Point2D'
    # перегрука модуля - возвращает также модуль чимлса типа complex типи вектора
    def __abs__(self):
        return hypot(self.coord[0], self.coord[1])

if __name__ =='__main__':
    point1 = Point2D(3,4)
    print('------метод объекта возращает дистанцию---------')
    # print(len(point1))
    print(point1.distance())
    print('------------итерация по объектам--------------')
    print('Лежит ли значение(координата) точки  в объекте:', 1 in point1, 2 in point1)
    print('Теперь можем и проитерироваться')
    for coord in point1:
        print(coord, end=' ')
    point2 = Point2D(1,8)
    print('')
    print('------ перегрузка равенства---------')
    print(point1 == point2)
    print('------перегрзука сравенения     lt от англ. «less than» — «меньше чем».-----------')
    print(point1 < point2)
    # print(point1.d, point2.d)
    print(point1.distance(), point2.distance())
    print('------перегрузка сравнения      le от англ. «less equal» — «меньше равно» ---------------------')
    print(point1 <= point2)
    print('------перегрузка больше равно   ge от англ. «greater equal» — «больше равно» ')
    print(point1 >= point2)
    print('-----перегрузка больше---------gt от англ. «greater than» — «больше чем»')
    print(point1 > point2)
    print('-----перегрузка сложения------- ')
    print(point1 + point2)
    print('-----перегрузка умножения--------')
    print(point1 * point2)
    print('-----перегрузка модуля')
    print(abs(point1))