from Class_point2D import Point2D
# Часть 2
# в одном будем редактировать класс в другом проверять

if __name__ == '__main__':
    # реализуем метод сравнения объектов ( создадим два объекта одинаковых вначале)
    point1 = Point2D(1, 1)
    point2 = Point2D(1, 2)
    # и выведим на экран результат их сравнения как равентсва
    print(point1 == point2)  # False т.е они не равны
    # ПОЧЕМУ РАБОТАЕТ? ответ потому что операция сравнения  наследуется из общего для всех класса  - это класс  objects
    # равенство будет только тогда когда равны объекты целиком
    print( point1 < point2 )
    # TypeError: '<' not supported between instances of 'Poin2D' and 'Poin2D'

# ПЕРЕГРУЗИМ СЛОЖЕНИЕ TypeError: unsupported operand type(s) for +: 'Poin2D' and 'Poin2D'
    print(point1 + point2) # Point: (2, 3)

# Еще вариант сложения - хотим единичку прибавить к каждой координате AttributeError: 'int' object has no attribute 'coord'
    print( point1 + 1) # Point: (2, 2)

# # ПОПРОБУЕМ ПРИВЕДЕНИЕ ТИПА к int  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'Point2D'
    print(float(point1))   # 1.4142135623730951