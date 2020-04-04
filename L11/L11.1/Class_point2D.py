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