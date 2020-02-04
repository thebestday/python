import random
import functools
import datetime


print("Задача 1")
# 20 имен
names = 'Vlad Ksenia Ilya Ivan Kostya Kosmos Katya Darya Valya Nikita Serezha Vitya Sarah Petya Victor Seva Ludmila Maksim Vova Raya'.split()
list_random_names = []
newName = ''

def NameList(names, n):
    '''
    :param names: список имен
    :param n: длина списка на выходе
    :return: список из 20 случайных имен
    '''
    for i in range(0, n):
        # random_number - это случайное число в пределах от до 20 включительно
        random_number = random.randint(0, len(names) - 1)
        # newName - это имя по случайно выбранному индексу(который получен генерацией случайного числа) из списка names
        newName = names[random_number]
        # добавляем случайное имя в список
        list_random_names.append(newName)

    return list_random_names

list_random_names = NameList(names, 100)

print('Список: \n',  list_random_names)

print()
print("Задача 2")
d = {}

def common_name(list):
    for i in list:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    print(d)
    print('-------------------------------------')
    x = sorted(d.items(), key=lambda x: -x[1])
    print(x)
    return x[0][0]

print(common_name(list_random_names))

print()
print("Задача 3")

def rare_letter(list):
    out = []
    for i in list:
        out += i[0]
    w = sorted(out)
    #print(w, type(w))
    drl = {a: w.count(a) for a in w}
    print(drl, type(drl))

    m = min(drl.values())
    print(m)
    # берем ключи по мин-ому значению
    m_keys = [k for k in drl if drl[k] == m]
    return m_keys
    # или первый ключ с минимальным значением (их может быть несоклько)
    # return m_keys[0]
print(rare_letter(list_random_names))

# 2 способ  метод это most_common ( но посчитать наимение распространненые)

# from collections import Counter
# def rare_letter(list):
#     out = []
#     for i in list:
#         out += i[0]
#
#     counter = Counter(out)
#
#     return counter.most_common()[-1:]
#
# print(rare_letter(list_random_names))





print()
print("Задача 4")

with open('log', 'r') as f:
    logs = f.read().splitlines()

array = list(map(lambda l: l.split(',')[0], logs))

latest_date = functools.reduce(lambda x, y: x if y < x else y, array)
print(latest_date)