import json

# Создадим объект json сделаем это из dict
dict_ex = {'brand': 'Volve', 'Price': 1.5, 'Vol': 2.0}
print(type(dict_ex), dict_ex)
# метод которым можно привести к типу json называется dumps()

# dumps()
# ПОЛУЧАЕМ ОБЪЕКТ ТИПА json
dict_to_json = json.dumps(dict_ex)
print(type(dict_to_json), dict_to_json)
# <class 'str'> {"brand": "Volve", "Price": 1.5, "Vol": 2.0}
# видим что данные сконвертировались  в строку - и теперь мы не можем обращаться по ключу
# не можем использовать dict-ие различные функции
#  сериализация - первод данных в удобный формат
# вы действительно можете использовать функцию eval() из JavaScript чтобы «декодировать» данные сериализованные в json

# теперь мы можем его записать в  файл
# что бы записать  нужун метод dump()
# dump()
with open('dict_to_json.txt', 'w') as f:
    json.dump(dict_ex, f)

# теперь будем принимающей стороной
# прочитаем этот файл из создадим снова из него словарь для дальнейшей работы
# ДЛЯ ОБРАТНОЙ КОНВЕРТАЦИИ МЕТОДЫ load() и loads()

# открываем файл на чтение в менедэере контекстов
# записываем в переменнцю то что вернет фун=я load()
with open('dict_to_json.txt') as f:
    data = json.load(f)
print(type(data), data)
# <class 'dict'> {'brand': 'Volve', 'Price': 1.5, 'Vol': 2.0}

# loads()
data1 = json.loads(dict_to_json)
print(type(data1), data1)
# <class 'dict'> {'brand': 'Volve', 'Price': 1.5, 'Vol': 2.0}



# ПРИМЕР РАБОТЫ С ДАННЫМИ json
# ответ по API
# запрос делаем и получаем ответ
import requests

# делаем get запрос к данному порталу
response = requests.get("https://jsonplaceholder.typicode.com/todos")
# responce обьъет ответа - там несколько параметров (text)
# серилизуем этот ответ с помощью команды json.loads и помещаем ответ в переменную data2
data2 = json.loads(response.text)
print(type(data2), data2)
# получаем спискок с json- чиками

