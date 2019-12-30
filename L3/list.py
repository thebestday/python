print("3.2 СПИСКИ1 Простейшие операции со списками")
# ОБъект list  СПИСКИ - СПИСКИ В ОТЛИЧИИ ОТ СТРОК ЭТО ИЗМЕНЯЕМЫЙ ТИИ ДАННЫХ универсальный инструмент для хранения любого вида объекта
print("------------------list представляет из себя массив")
# доступ к объету листа ( можно обратиться по индексу) получить значение  так же у листов предусмотрены срезы все то же самое как и у строк
List = [0, 1, 2, 4, 5]
print(type(List), List)
# классная вещь в питоне это ГЕНЕРАЦИЯ СПИСКОВ [ x**2 for x in num if x > 0]
# т.е сразу делаем и отсев(УСЛОВИЕ В КОНЦЕ) и фильтрацию и пременение функции(НАХОДИТСЯ В САМОМ НАЧАЛЕ - генараторы списков)
# центральная часть этого генератора это те x-сы  по которым осуществляем перебор из массива num
print("------------------ПУСТОЙ СПИСОК")
# ПУСТОЙ СПИСОК ГЕНЕРИРУЕТСЯ С ПОМОЩЬЮ Квадратных скобок
list_temp = []
print(type(list_temp), list_temp)

print("------------------список можно заполнять любыми объектами, делается это через запятую") # список можно заполнять любыми объектами, делается это через запятую
list_temp = [1.2, 2, 123, 'Volvo', [1,2,3]]
print(type(list_temp), list_temp)

print("------------------пройдемся по элементам списка") #пройдемся по элементам списка
for el in list_temp:
    print(el, type(el))

print("----------------инициализировать список можно с помощью команды list из строки" ) # также инициализировать список можно с помощью команды list (это похоже на приведение типов)
list_str = list('Volvo')
print(list_str)
#у нас строка представилась в виде отдельных букв и каждая отдельная буква представляет собой элемент списка list_str

print("------------------Обращение к элементам списка, подсписки") # Обращение к элементам списка, подсписки (так же как и у строк)
for i in range(len(list_str)):
    print(i, ':', list_str[i])


print("-----------------срезы c i -того элемента и до конца") # срезы (тоже в цикле сделаем) c i -того элемента и до конца
for i in range(len(list_str)):
    print(i, ':', list_str[i:])


print("-----------------срезы c начала и до i -того элемента") # срезы (тоже в цикле сделаем) c начала и до i -того элемента
for i in range(len(list_str)):
    print(i, ':', list_str[:i])

print("---------------- Функции со списками ")
print("---------------- Функция len() ") # Функции со списками (len() универсальная функция которая подразумевает длину объекта)
print(len(list_str))


print("---------------- Операции со списком ")
print("---------------- Операция + т.е фактически конкатенация двух списков")# Операция + т.е фактически конкатенация двух списков
print(list_temp + list_str)

print("----------------внешнее умножнение на целые числа ")
# и доступно внешнее умножнение на целые числа (в примере из двух списков создался один список)
print(list_temp*2)

print("----------------Методы ")# Методы важная тема для списков 8-24
# append это метод для добавления в конец

print("----------------append наполним список в цикле целыммы числами ")
integer_list = []
for i in range(5):
    integer_list.append(i)
print(integer_list)

print("----------------добавим в конец число 100 с помощью append")
integer_list.append(100)
print(integer_list)

print("--------метод remove (по сути удаление первого встретившегося соответствующего элемента)")#  удаляет первый элемент по вхождению")
#  удаляет первый по вхождению элемент
integer_list.remove(100)
print(integer_list)

print("--------del integer_list[4] удалить элемент по его индексу") # del integer_list[4] удалить элемент по его индексу
del integer_list[4]
print(integer_list)

print("-------Встроенная функция reversed()")# reverse изменить порядок - НУЖНО ДЕЛАТЬ ВНАЧАЛЕ (чтобы метод применился) - ПОТОМ print
integer_list.reverse()
print(integer_list)

print("-------sort это метод сортировки листа в порядке возврастания")# sort это метод сортировки листа в порядке возврастания
integer_list = [9, 3, 6, 2, 4]
integer_list.sort() # нужно делат вначале а только потом выводить на экран
print(integer_list)

print("--метод insert принимает на вход 2 параметра(позициякудавтавлять, точтобудемвставлять)") # insert(позициякудавтавлять, точтобудемвставлять)
integer_list.insert(2, 100)
print(integer_list)

print("-----------------------3.3 СПИСКИ2 ПРОДОЛЖНЕИЕ ----------------------------")
print("---- функция map принимает два аргумента: функцию и аргумент составного типа данных, например, список.")# функция map принимает два аргумента: функцию и аргумент составного типа данных, например, список.
# например мы хотим каждый элемент списка возвести в квадрат
# но сначла нужно привести к типу list
# НЕОБХОДИОМ ПРИМЕНИТЬ ПРИВЕДЕНИЕ ТИПОВ т.к тиа map возвращает другой тип - map
integer_list = [9, 3, 6, 2, 4]
print(type(integer_list), integer_list)
# map(function, list) ----> map -----> list(map)
# функция str применяется к каждому элементу  integer_list
new_integer_list = list(map(str, integer_list))   # привели данные к типу строка
print("----привели данные к типу строка---")
print(type(new_integer_list), new_integer_list)     # каждый элемента стал строкой

print("возведение в квадрат с помощью  lambda Лямбда-функция — это небольшая анонимная функция")# lambda x , каждому элемнту х применяется функция хх*2
new_integer_list = list(map(lambda x: x**2, integer_list))
print(type(new_integer_list), new_integer_list)


print("---функция фильтр - фильтрация списка согласно некоторому условию---")# функция фильтр - фильтрация списка согласно некоторому условию
# придется применить функцию лямбда для фильтрации списка
# filter  т.е. которые меньше 5 остаются в новом списке
new_integer_list = list(filter(lambda x: x < 5, integer_list))
print(new_integer_list)

print("---reduce применяется ко всем элементам спискаи возвращает один элемент-- ")# reduce применяется ко всем элементам списка и возвращает один элемент
# например найдем сумму данного списка с помомощью функции reduce()
# х - это то что было
# у - это новый элемент
from functools import reduce
integer_list = [1,2,3,4]
print(type(integer_list), integer_list)

print("---Найдем с помощью операции reduce сумму элементов данного списка integer_list-- ")# Найдем с помощью операции reduce сумму элементов данного списка integer_list
sum = reduce(lambda x, y: x + y, integer_list)
print(type(sum), sum)

print("---Найдем с помощью операции reduce  произведение элементов данного списка integer_list-- ")# Найдем с помощью операции reduce произведение  элементов данного списка integer_list
product = reduce(lambda x, y: x * y, integer_list)
print(type(product),product)

