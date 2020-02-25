# Тернарный оператор
# сначала напишем функ-ю
age = 17
def check_adult(age):
    check = 0
    if age >= 18:
        check = 1
    else:
        check = 0
    return check
print(check_adult(age))



check = 1 if age >= 18 else 0
print(check)

# или  через lambda функцию
check_adult_l = lambda x: 1 if age>= 18 else 0
print(check_adult_l(age))


# Генераторый последовательностей
# Генератор списка
list_sq1 = []
list_sq2 = []
N = 10
for i in  range(1, N + 1):
    list_sq1.append((i**2))
    list_sq2.append((i ** 2) % 10)
print(list_sq1, list_sq2)

# теперь с помощью генераторв списка
list_sq1_g = [(i**2) for i in range(1, N + 1)]
list_sq2_g = [(i**2) % 10 for i in range(1, N + 1)]
print(list_sq1_g, list_sq2_g)

# Громозкость кода появляется если еще добаляется условие if
# добавим условие в нашу функцию
list_sq = []
N = 10
for i in  range(1, N + 1):
    if (i**2) % 2 == 0:
        list_sq.append(i ** 2)
# print(list_sq)

list_sq_g = [(i**2) for i in range(1, N + 1) if (i**2) % 2 == 0]
print(list_sq, list_sq_g)

# Генератор словаря
dict_g = {i: i**2 for i in range(1, N+1)}
print(dict_g)
# Генератор множества- но без двоеточия (значени будут в случайном порядке)
set_g = { i**2 for i in range(1, N+1) }
set_g_d = {(i**2) % 10  for i in range(1, N+1)}
print(set_g, set_g_d)

# Решим задачу - у нас есть список имен
list_names =['Dima', 'kate', 'OLeg', 'natali']
# сформируем список из первых букв так, что бы они были бы заглавными
# будем использовать тернарный оператор и генератор списка одновременно
list_char = [x[0] if x[0].isupper() else x[0].title() for x in list_names]
print(list_char)
print('вернули первые буквы заглавными')