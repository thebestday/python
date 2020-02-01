# map
def miles_to_km(miles):
    return miles * 1.6



mile_dist = [1.0, 1.6, 2.3]

km_dist = list(map(miles_to_km, mile_dist))
print(type(km_dist ), km_dist )

# решим пример что выше с помощью lambda
km_dist = list(map(lambda x: 1.6 * x, mile_dist) )
print(type(km_dist ), km_dist )

#  в map можно подавать на вход два даже три списка, тогда ф-я которая стоит на первой позици должна принимать два аргумента
# map сделает операцию почеленно с каждым списком
list_1 = [1,2,3]
list_2 = [4,5,6]

list_3 = list(map(lambda x,y: x * y, list_1, list_2))
print(list_3)
list_3 = list(map(lambda x,y: x * y, list_1, list_2))
print(list_3)

# reduce сначла импорт начиная с python3 +
# найдем максимальный элемент в листе
from functools import  reduce
list_temp = [43, 12, 41, 100, 101, 4]
max = reduce(lambda a,b: a if a > b else b, list_temp)
print(max)

# filter
# отсортируем - найдем элементы больше 50 после : сразу пишем условие
list_50 = list(filter(lambda x: x > 50, list_temp))
print(list_50)
# отсортируем - найдем элементы у которых остаток от деления на 10 равен 1
list_50 = list(filter(lambda x: x % 10 == 1, list_temp))
print(list_50)

# sorted это ф-я которая на вход принимает список и возвращает так же список - нужно создавать для ее новый список
list_temp_sort = sorted(list_temp)
print(list_temp_sort)
# попробуем сортировку в обратном порядке - по убыванию
# для этого ставим параметр reverse = TRue
list_temp_sort_reverse = sorted(list_temp, reverse = True)
print(list_temp_sort_reverse)

# сортировка по ключам - для этого создадим другой список - отсортирумем лист из строк
list_names = ['Kate', 'Dima', 'Ivan', 'Mike']
# применим ф-ю сортировки сначала без ключей в обычном виде
# упорядочивание будет происходить в алфавитном порядке
list_names_sorted = sorted(list_names)
print(list_names_sorted)

# ДОпустим мы хотим по 2 букве данный список -для этого нужно указать спец-ю ф-ю которая нам покажет что будет сортировать по 2 букве
# указыаем ключ - это и есть параметр по которому  будет происходить сортировка - называется ключом
list_names_sort_key = sorted(list_names, key = lambda x: x[1])
print(list_names_sort_key)
