# Часть 1
class Point2D():
    def __init__(self, x, y):
        self.coord = [x,y]

    def __str__(self):
        return (f'Point: ({self.coord[0]}, {self.coord[1]})')


    def __del__(self):
        del self.coord

     # ОПРЕДЕЛЯЕМ ПОВЕДЕНИЕ КЛЮЧЕВОГО СЛОВА in
    # вообще итеририроваться можно по любому объекту - для этого нужно определить что значить in
    # что бы проверять - что бы работал метод in
    # необходимо определить следующий метод класса -метод get.item - но для ЭТОГО НУЖНО ЧТО БЫ БЫЛ ИТЕРИРУЕМЫ АТРИБУТ self.coord = [x,y] - так правильно лист из координат
    # self.coord1 = 1 self.coord2 = y - так не правильно

    def __getitem__(self, key):
        return self.coord[key]

    # Доопределить в классе реакцию на ф-ю len
    # необходимо что бы был вектор (длина точки это неопределенное понятие) у ветора есть длина -расстояние от точки до 0
    # Этот пример - не корректный - некооректно использовать длину len(point1) ТАК КАК НУЖНО ПРИВОДИТЬ К int ('float' object cannot be interpreted as an integer)
    def __len__(self):
        return int((self.coord[0]**2 + self.coord[1]**2)**0.5)
    # делаем обычный метод для этой же цели
    def distance(self):
        return (self.coord[0]**2 + self.coord[1]**2)**0.5


# Часть 1 -------------------------------------------
# Часть 2 -------------------------------------------
# Напишем магический метод который будет выполняться при операции сравнения  # Будем сравнивать точки покоординатно
# ПЕРЕГРУЗКА РАВЕНСТВА
    def __eq__(self, other):
        return (self.coord[0] == other.coord[0])&(self.coord[1] == other.coord[1])
 # теперь print(point1 == point2) возвращает True

# перегрузка больше меньше(< знак ) TypeError: '<' not supported between instances of 'Poin2D' and 'Poin2D'
# ПЕРЕОПРЕДЕЛИМ МЕТОД  __lt__
# сравнивать точки будем по расстоянию   # True
    def __lt__(self, other):
        return (self.distance() < other.distance())

# ПЕРЕГРУЗИМ СЛОЖЕНИЕ TypeError: unsupported operand type(s) for +: 'Poin2D' and 'Poin2D'
# + не поддерживается в класс point2D - необходимое его переопределить
# МЕТОД __add__ возвращет объект этого же класса (так же можно переоперделить *  /  )
    def __add__(self, other):
        if isinstance(other, Point2D):
            return Point2D(self.coord[0] + other.coord[0], self.coord[1] + other.coord[1]) # (2, 3) сложили покоординатно
        # Еще вариант сложения - хотим единичку прибавить к каждой координате AttributeError: 'int' object has no attribute 'coord'
        if isinstance(other, int):
            return Point2D(self.coord[0] + other, self.coord[1] + other)  # Point: (2, 2)


# # ПОПРОБУЕМ ПРИВЕДЕНИЕ ТИПА к int  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'Point2D'
# # float проще т.к как там будет длина вектора
# Point2D ->  float
    def __float__(self):
        return self.distance() # 1.4142135623730951

# Часть 3 ---------------------------------------------
# поможем pickle правильнло сериализовать и десериализовать этот объект data
# для этого определим два магических метода
# Первый магический метод __getstate__ который при сериализации сохранит некоторую информацию об объекте
# насм необходимо сохранить список self.coord
    def __getstate__(self):
        return self.coord
# Второй магический метод __selfstate__(self, state) принимает состояние которе будет передано из метода _getstate__
# с помощью метода __setsafe__ будет произведена десериализация
# присвоим значения self.coord  state - список из двух занчений точек (в данном случае)
    def __setstate__(self, state):
        self.coord = state

# getstate вытаскиваем необходимые атрибуты класса
# setstate метод который при десериализации настраивает  - присваивает некоторые значения атрибуту

# Часть 4
# статические методы - что бы написат с.м. необходимо написат фу-ю

# НО НА ВХОД НЕ ПОДАЕТСЯ ПАРАМЕТР self и чтобы компилятор не ругался делают специальный декоратор
# ЧТО МОЖНО ПРИДУМАТЬ - подаем например координаты x, y (не точку)
# будет ли расстояние до данного вектора больше 1
    @staticmethod                  # теперь это считается статистической  функ-ей данного класса
    def stat_method_ex(x, y):
        if (x**2 + y**2)**0.5 > 1:
            return 1
        return 0

# метод класса - декоратор для этого используется @classmethod
    @classmethod
    def class_method_ex(cls):         # cls на вход подается клвсс cls
        point_list = []
        for i in range(10):
            point_list.append(cls(i, i + 1))
        return point_list

#  Стат.методы это некотрые вспомогательные ф-и  - на вход подаются просто некоторые параметры и не подаются не объект и не класс
#   Методы классов  используются для генерации каких -то последовательностей специальных объектов  - на вход подается сам класс



if __name__ == '__main__':
# вызовем метод класса
# т.к это метод класса( не метод объекта) то  он вызвывается через class.данныйметод
    list_ = Point2D.class_method_ex()
    print(list_)          # выведет объекты - эти точки
    for i in range(10):
        print(list_[i])

# Вызываем статичекий метод
    print(Point2D.stat_method_ex(1,2))               #1 у вектора(1,2) расстояние больше 1
