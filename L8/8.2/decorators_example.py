# ПРОСТОЙ ДЕКОРАТОР(без параметров)
# Ф-я принимает на вход ф-ю
# она возвращает ф-ю до которой стоит какой-то код и после которой стоит какой-то код
# создадим в ней другую ф-ю называемой оберткой
# def show_information(f):
#     def wrapper():
#         print('Code before function')
#         f()
#         print('COde after function')
#     return wrapper


# def simple_function():
#     print("I'm simple function")
#
# simple_function()
#
# simple_function_decorated = show_information(simple_function)
# simple_function_decorated()

# Using decorations
def show_information(f):
    def wrapper(*args, **kwargs):
        print('Code before function')
        f(*args, **kwargs)
        print('COde after function')
    return wrapper

@show_information
def another_simple_function():
    print('I`m simple function too')

another_simple_function()

# Декораторы с параметрами
def show_type(f):
    def wrapper(*args, **kwargs):
        print('Тип переменной 1', type(args[0]))
        print(f(*args, **kwargs))
        print('Тип переменной 2', type(args[1]))
    return wrapper

@show_information
@show_type
def my_add(a,b):
    return a+b

my_add(10, 20)

# Еще пример декоратора (может быть каскадный)
# вывод времени работы ф-и

import time
import requests

def show_time(f):
    def wrapper(*args, **kwargs):
        print(time.time())
        print('URL: ', args[0])
        print(f(*args, **kwargs))
        print(time.time())
    return wrapper

@show_time
def requests_example(url):
    webpage = requests.get(url)
    return webpage.text

url = "https://google.com"

requests_example(url)



