print('----3.4 Словари ---')
# Инициализация словарей -
print('----пустой словарь инициализируется фигурными скобками {} ---')
dict_temp = {}
print(type(dict_temp), dict_temp)

print('---словарь наполненный некоторыми (объектами) парами ключ-значение где все значения имеют разные типы----------')# сделаем словарь  наполненный некоторыми объектами где все значения имеют разные типы
dict_temp = {'key1': 1, 'key2': 2.1, 'key3': 'name', 'key4': [1,2,3]}
print(type(dict_temp), dict_temp)
print('')
print('----еще один метод инициализации словарей  dict.fromkeys - метод fromkeys()---')# еще один метод инициализации словарей  dict.fromkeys
print('dict это класс; fromkeys это метод')  # dict это класс; fromkeys это метод
print('Метод fromkeys() создает новый словарь с ключами в seq и значений, установленных в value.')
print('синтаксис для метода fromkeys():  dict.fromkeys(seq[, value]))')
print('будет создан словарь у которого ключами являются элементы a  и b ;  а значения будут пустыми')# будет создан словарь у которого ключами являются элементы a  и b ;  а значения будут пустыми

dict_temp = dict.fromkeys(['a','b']) # при заданном value, значением каждого элемента словаря явится один и тот же экземпляр
print(type(dict_temp), dict_temp)
print(' fromkeys(seq[, value]) -> dict Новый словарь, созданный из последовательности. Этот метод возвращает список.')# fromkeys(seq[, value]) -> dict Новый словарь, созданный из последовательности.
print('    ')

print('----dict.fromkeys фактически для создания ключей а потом для насыщения словаря пaрами ключ-значения---')
print("что бы наполнить значениями нужно подать еще одни список dict_temp = dict.fromkeys(['a','b'], 10)---")# что бы наполнить значениями нужно подать еще одни список
print('-----присвоит каждому ключу значение 10 - НУ ТАКОЙ МЕТОД - КАЖДОМУ РАЗНЫЕ НЕЛЬЗЯ СРАЗУ ЖЕ ЗНЕЧЕНИЯ ПЕРЕДАТЬ ------ ')
dict_temp = dict.fromkeys(['a','b'], 10) # присвоит каждому ключу значение 10
print(type(dict_temp), dict_temp)

print('')
print('------Ещё одни пример показывает использование метода fromkeys().')
seq = ('name', 'age', 'sex')
dict1 = dict.fromkeys(seq)
print ("Новый словать : %s" %  str(dict1))
dict2 = dict.fromkeys(seq, 18)
print ("Новый словарь : %s" %  str(dict2))


print('')
print('----метод просто dict() для создания словаря (здесь вводим ключ- значение) dict(brend = "volvo", volume_engine = 1.5)  ------')
#Если необходимо создать словарь с заранее подготовленным набором данных, но с перечислением групп ключ-значение -- функция dict()
dict_temp = dict(brend ='volvo', volume_engine = 1.5)
print(type(dict_temp), dict_temp)

print("----обращение к содержимому словаря происходит по ключу ( у него нет номера) print(dict_temp['brend']) ---")
# обращение к содержимому словаря по ключу
print(dict_temp['brend'])
print(dict_temp['volume_engine'])

print('')
print('----инициализировать словарь с помощью генератора ---')# мы можем инициализировать словарь с помощью генератора
print("dict_temp = {a: a**2 for a in range(10)} #ключ a для которого значение будет a в квадрате для а в range(10)")
dict_temp = {a: a**2 for a in range(10)} #ключ a для которого значение будет a в квадрате для а в range(10)
print(type(dict_temp), dict_temp)
print('----обращение к содержимому словаря происходит по ключу [8] ---print(dict_temp[8])')
print(dict_temp[8]) # как будьто индекс но на самом деле это ключ

print('')
print('----обращение к содержимому словаря  ---')
print('----часто бывает необходимо знать все ключи словаря и все значени ---')# Обращение к содержимому часто бывает необходимо знать все ключи словаря и все значения)

print('----ФУНКЦИИ СО СЛОВАРЯМИ ---')
# Получим все ключи словаря  функция keys()
print('----функция keys() возвращает специальный тип - называется dict_key который содержит все ключи ---print(dict_temp.keys()) ')# функция возвращает специальный тип - называется dict_key который содержит все ключи
print(dict_temp.keys()) # dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('----но как правило с типом dict_keys не работают и его приводят к типу list -------------------print(list(dict_temp.keys()))')# но как правило с этим типом не работают а приводят к типу list
print(list(dict_temp.keys())) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('-ВСЕ НЕОБХОДИМЫЕ ОПЕРАЦИИ НЕОБХОДИМО ПРОЗВЕСТИ С КЛЮЧАМИ - ИХ ДЕЛАЮТ С LIST -ом ---')# все необходимые операции которые необходимо произвести с ключами их делают с list -ом
print('--функция values() возвращает специальный тип - называется dict_values который содержит все значения --print(dict_temp.values()) ')
print(dict_temp.values()) # dict_values([0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
print('----но так же можно получить значения --------------- -----------------------------------------------print(list(dict_temp.values()))')# но так же можно получить значение в объекте list
print(list(dict_temp.values())) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(' ')
print('----ВСЕ МЕТОДЫ КОТОРЫЕ ЕСТЬ В list-ах вы можете использовать при работе C КЛЮЧАМИ И ЗНАЧЕНИЯМИ ---')
print(' ')

print(' ')
print('----Так же можно работать с парами ключ-значение для этого необходимо использовать метед items() ---')
print('МЕТОД items() -  метод возращает кортежи - лист кортежей ')
print(' кортеж это тот же самый лист только неизменяемый print(list(dict_temp.items())) ')
print(list(dict_temp.items())) # кортеж это тот же самый лист только неизменяемый
print(' ')


print('')
# РАБОТА С ЭЛЕМЕНТАМИ - НАМ НЕОБХОДИМО ПОЛУЧАТЬ ЗНАЧЕНИЕ, ИЗМЕНЯТЬ(словарь это изменяемый тип) и ДОБАЛЯТЬ НОВОЕ ЗНАЧЕНИЕ
print('пример - нулевому ключу изенили значени на 100 (было значение 0) -------  dict_temp[0] = 100        ')
dict_temp[0] = 100# присвоим нулевому ключу другое значение = 1000
print(type(dict_temp), dict_temp)

print('')
print(' можем добавлять какие-то значение -делается это путем присваивания')# можем добавлять какие-то значение -делается это путем присваивания
print("например несуществуещему ключу name присвоим значение Dima ------------- dict_temp['name'] = 'Dima'")# например несуществуещему ключу name присвоим значение Dima
dict_temp['name'] = 'Dima'
print(type(dict_temp), dict_temp)

print('')
print(' МОжно удалять значение по ключу - метод pop() УДАЛЯЕТ КЛЮЧ И ВОЗРАЩАЕТ ЗНАЧЕНИЕ(ЕСЛИ КЛЮЧА НЕТ- то возращает DEFAuLT ничего и не создает ошибку !!!!!!!!!!!!!11')
print(" метод pop() УДАЛЯЕТ КЛЮЧ И ВОЗРАЩАЕТ ЗНАЧЕНИЕ которое удалил ------- print(dict_temp.pop('name'))")
temp = dict_temp.pop('name')
print(temp)  # dict_temp.pop('name') ВОЗРАЩАЕТ ЗНАЧЕНИЕ которое удалил
print(type(dict_temp), dict_temp)



print('')
# МЕТОД ОГРОМНОЕ МНОЖЕСТВО (часть уже рассмотрели выше - это keys() values() items() см выше
# Словарь можно очищать копировать
# МОжно удалять значение по ключу - метод pop() УДАЛЯЕТ КЛЮЧ И ВОЗРАЩАЕТ ЗНАЧЕНИЕ !!!!!!!!!!!!!11

print('ИТЕРИРОВАНИЕ ПО СЛОВАРЮ ')
# МОЖНО ИТЕРИРОВАТЬСЯ ПО СЛОВАРЮ
# ИТЕРИРОВАТЬСЯ МОЖНО ТАК ЖЕ КАК И ПО СПИСКАМ

# ИТЕРИРОВАНИЕ ПО СЛОВАРЮ ПО КЛЮЧУ И ПО ЗНАЧЕНИЮ
print('МЫ ПО ПАРАМ КЛЮЧ ЗНАЧЕНИЯ ИТЕРИРУЕМСЯ В СЛОВАРЕ dict_temp.items()') # МЫ ПО ПАРАМ КЛЮЧ ЗНАЧЕНИЯ ИТЕРИРУЕМСЯ В СЛОВАРЕ dict_temp.items()
for pair in dict_temp.items():
    print(pair)

print('')
print("pair это пара но удобнее работать с конкретными элементами - ключом и его значением") # pair это пара но удобнее работать с конкретными элементами - ключом и его значением
for key, value in dict_temp.items():
    print(key, value)

print('')
print('Можно итерироваться и по ключам') # можно итерироваться и по ключам
for key in dict_temp.keys():
    print(key)

print('')
print('Можно итерироваться и по значениям')# можно итерироваться по значениям
for value in dict_temp.values():
    print(value)