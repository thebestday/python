class Point2D:
    # специальный метод - метод init это инициалазатор
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # вывод напишем имя класса - что будет выполняться при print
    def __str__(self):
        return f'Точка: ({self.x}, {self.y})'
    def distance(self):
        return (self.x**2 + self.y**2)**0.5
    # напишем более сложную ф-ю расстояние до другой точки
    def point_distance(self, a, b):
        return ((self.x-a)**2 + (self.y-b)**2)**0.5
    # перегрузка "+" метод для перегрузки сложений объектов
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

p = Point2D(2, 3)

print(p.x, p.y)
print(p.distance())
print(p.point_distance(2,3))
print(p.point_distance(3,4))
q = Point2D(3, -2)
print(p + q)
print(p)
# print(p, type(p))
