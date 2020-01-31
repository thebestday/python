# Занятие 4.1
# return что угодно
# функция может возращать лююые объекты в питоне( массивы, кортежи, списки,словари_и т.д)
# кода присваиваем входной переменной значение - то эта переменная СТАНОВИТЬСЯ НЕ ОБЯЗАТЕЛЬНОЙ
# т.е в данную функцию можно передавать только два значения a и b , значение с будет по умолчанию равен 2
def function(a,b,c = 2):
    return a + b + c
print(function(3, 4))

print('-------------ПРОСТАЯ ФУНКЦИЯ')
def add(x,y):
    '''
     :param x;
     :param y;
     :return
    '''
    return x + y

#    z = x + y
#    return z
# что бы посмотрет описание фунции нужно вызвать метод help
help(add)
print((add(100, 101)))
print((add('Dima', '+Kate')))

# Давайте вернем функцию из функции
def f1(n):
    def f2(m):
        return n + m
    return f2

# инициализируем значение n = 100
new_f = f1(100)
print(type(new_f), new_f)

print((new_f(250))) # получили 350

print('функция может ничего не возвращать ')
def f():
    pass
print(f()) # None
# АРГУМЕНТЫ
def add(x,y, z = 10):
    return x+y+z
print(add(1,2)) # 13
print(add(1,2,3)) # 6

# 1 можем передават  любое значение параметрв с помощью специального массива args
def func(*args):
    print(type(args), args)
    return args

func(1,2,3,"Volvo") # <class 'tuple'>, (1, 2, 3, 'Volvo')
# 2 можем передавать параметры с помощью словаря dict
def func(**kwargs):
    print(type(kwargs), kwargs)

func(a = 1, b = 2, c = 'Volvo', d = 1.5) # <class 'dict'> {'a': 1, 'b': 2, 'c': 'Volvo', 'd': 1.5}

# можно создать сложные на вход стуктуры параметров
def func_difficult(x, y = 2, *args, **kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(args), args)
    print(type(kwargs), kwargs)

func_difficult(1,3, (1,2,3), temp = 12, temp1 = 13)
# ТО ЧТО ВЕРНЕТ ФУНКЦИЯ
# <class 'int'> 1
# <class 'int'> 3
# <class 'tuple'> ((1, 2, 3),)
# <class 'dict'> {'temp': 12, 'temp1': 13}


