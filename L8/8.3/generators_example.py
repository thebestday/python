# Необходимость использования генераторов возникает когда осуществляется перебор большого числа объектов
# возникает ситуация хранить большое количество информации в памяти   - что не удобно - забивается кеш -снижатеся производительность
# найти все записи в 1000000 значений
# генератор каждый раз выхватыает по одному элементу из того множества по которому осуществляется перебор
# пример простого генератора - называется счет вниз
# yield вычисление следующего значкения генератора
# def countdown(num):
#     print('Starting')
#     while num > 0:
#         yield num
#     num -= 1
#
# print(countdown(15))
import sys
# почувствуем разницу м\ду ГЕНЕРАТОРАМИ СПИСКОВ и ПРОСТО ГЕНЕРАТОРАМИ
simle_list = [x**3 for x in range(20)]
print(type(simle_list))
for i in simle_list:
    print(i)

print('Memory:', sys.getsizeof(simle_list))
# ВИДИМ ЧТО У ЛИСТА ПАМЯТЬ РОСТЕТ ЛИНЕЙНО  С РОСТОМ КОЛЧЕСТВА ЭЛЕМЕНТОВ В ЛИСТЕ
# Теперь создаем ГЕНЕРАТОР
# НЕЯВНЫЙ ГЕНЕРАТОР - создается при помощи круглях скобок
# Неявный потому как не использует ни какие особые свойства генераторов
simle_generator = (x**3 for x in range(20))
print(type(simle_generator))
for i in simle_generator:
    print(i)

print('Memory:', sys.getsizeof(simle_generator))
# Генератор каждай раз вычисляет новый элемент - ему не нужно хранить все элементы в памяти

# ЯВНЫЕ ГЕНЕРАТОРЫ - ПРОСТОЙ ПРИМЕР
# ГЕНЕРАТОРЫ ОПРЕДЕЛЯЮТСЯ ЧЕРЕЗ ФУНКЦИИ
def generator_example_1(num):
    for i in range(num):
        yield(i**3)

gen = generator_example_1(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# ЯВНЫЕ ГЕНЕРАТОРЫ - СЛОЖНЫЙ ПРИМЕР
import time
import os
import random  # ДЛЯ СОЗДАНИЯ СПИСОКОВ
import psutil # модуль измеряет количество требуюмой памяти в кеше для выполнения каждой операции(каждого объекта)

colors =['White', 'Black', 'Green']
brands = ['Volve', 'Lada', 'Audi']
#
# def cars(num):
#     cars_list= []
#     for i in range(num):
#         car = {'color': random.choice(colors),
#                'brand': random.choice(brands),
#                'id':i}
#         cars_list.append(car)
#     return  cars_list
#
# # СОЗДАЕМ объем необходимый для вычисления памяти
# proc = psutil.Process(os.getpid())
# print('Память до вып. функции:' + str(proc.memory_info().rss/1000000))
# start= time.clock()
#
# cars_list = cars(1000000)
# print(cars_list)
# stop=time.clock()
#
# proc = psutil.Process(os.getpid())
# print('Память после вып. функции:' + str(proc.memory_info().rss/1000000))
# print('Заняло {} секунд'.format((stop - start)))
#

# СДЕЛАЕМ ТОЖЕ САМОЕ НО ПРИМЕНИМ ГЕНЕРАТОР
def cars_gen(num):
    for i in range(num):
        car = {'color': random.choice(colors),
               'brand': random.choice(brands),
               'id':i}
    yield car

# СОЗДАЕМ объем необходимый для вычисления памяти
proc = psutil.Process(os.getpid())
print('Память до вып. функции:' + str(proc.memory_info().rss/1000000))
start= time.clock()

cars_generator = cars_gen(1000000)
print(cars_generator)
stop=time.clock()

proc = psutil.Process(os.getpid())
print('Память после вып. функции:' + str(proc.memory_info().rss/1000000))
print('Заняло {} секунд'.format((stop - start)))
