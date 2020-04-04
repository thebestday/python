import pickle
# пробуем сериализоват объект класс
from Class_point2D import Point2D
# Создадим объект класса
point1 = Point2D(1,1)
# Создадим объект
# data = {'1': (1,2), '2': 'volvo', '3': True, '4': point1}



# Открываем файл для сериализации объектов Python
# f = open('data.pkl', 'wb')
# # сериализуем методом dump
# pickle.dump(data, f)
# f.close()
# Десериализация # ОТрываем файл в режиме rb
# f = open('data.pkl', 'rb')
# data_new = pickle.load(f)
# print(data)
# print(data_new)
# f.close()

# для метода  __setstate__(self, state) нужна сериализовать именно ОБЪЕКТ ( не в словаре объект)
# эти методы для сериализации объекта, через словарь не получается
f = open('point.pkl', 'wb')
pickle.dump(point1, f)
f.close()

f= open('point.pkl', 'rb')
point_new = pickle.load(f)

print(point1)
print(point_new)