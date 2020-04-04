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



if __name__ == '__main__':
    point1 = Point2D(1,1)
    print(point1)
    str1 = 'volvo'
    list_text = [1,2,3,4]
    print(len(str1), len(list_text), len(point1))
    print(point1.distance())
    for item in str1:
        print(item)

    # Если итерируемся по листу - то мы итериреуемся по ОБЪЕКТАМ КОТОРЫЕ ЛЕЖАТ В ЛИСТЕ
    for item in list_text:
        print(item)

    # теперь можно посмотреть лежит ли значение какой- то точки | есть ли координта 1 in point1
    print(1 in point1)
    print(2 in point1) # False те такой коодинаты нет
    # и теперь можно проитерироваться
    for coord in point1:
        print(coord)