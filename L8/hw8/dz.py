import time
import random
import sys

# 1. Написать декоратор, замеряющий время выполнения декорируемой функции.
print()
print('Задание 1. Декоратор, замеряющий время выполнения декорируемой функции.')
print()

def show_time(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        f(*args, **kwargs)
        stop_time = time.time()
        print('Время выполнения функции: {}'.format(stop_time - start_time))
    return wrapper

@show_time
def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    print(prod)

factorial(5)


#2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).

def time_list(n):
    list = [i for i in range(n)]
    return list

start_time = time.time()
func_list = time_list(1000001)
stop_time = time.time()
time_list = stop_time - start_time
memory_list = sys.getsizeof(func_list)
print('Время создания списка с элементами от 1 до 1000000: {}.\nОбъем оперативной памяти: {}'.format(time_list, memory_list))


def time_generator(n):
    for i in range(n):
        yield(i)

start_time = time.time()
func_gen = time_generator(1000001)
stop_time = time.time()
time_gen = stop_time - start_time
memory_gen = sys.getsizeof(func_gen)
print('Время создания генератора с элементами от 1 до 1000000: {}.\nОбъем оперативной памяти: {}'.format(time_gen, memory_gen))



if time_list - time_gen > 0:
    print('Генератор создался быстрее.')
else:
    print('Список создался быстрее.')

# 4. Сравнить объем оперативной памяти
if memory_list - memory_gen > 0:
    print('Список занимает больше оперативной памяти.')
else:
    print('Генератор занимает больше оперативной памяти.')


# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.

def show_memory(f):
    def wrapper(*args, **kwargs):
        print(f(*args, **kwargs))
        print('Объем занимаемой памяти: ', sys.getsizeof(f))
    return wrapper

@show_memory
def many(*args, **kwargs):
    print( args )
    print( kwargs )
many(1, 2, 3, name="Mike", job="programmer")
many(10, 20, 30, name="Vlad", job="writer")

