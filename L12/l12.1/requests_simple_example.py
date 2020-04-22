# простейший get запрсос с курсом валют
# requests самая популярная библиотека по оргранизации запросов
import requests
import pprint
# ссылка для доступа к API валют
# get запрос

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
# посмотрим какие методы и атрибуты есть у данного объекта models.Response  <class 'requests.models.Response'>
#  у объекта  models.Response  есть стандартные атрибуты   status_code   text  json
# response = requests.get(url)
# print(type(response), dir(response))
# status_code это некоторое возращаемое числа - говорит о том как завершился запрос к серверу (успешно 200 / обшка со стороны клиента начинается с 4 404/ ошибка с цифры 5 ошибка сервера
# print(response.text)           # пришли валюты

# ДЛЯ УТОЧНЕНИЯ ЗАПРОСОВ МЫ МОЖЕТ В get запрос передать некоторые параметры
# параметры передаются в словаре обычно назвается params
params = {
    'id': 'AUD'
}
# что бы сделать запрос с параметром нужно передать атрибут в метод get
response = requests.get(url, params = params)
print(response.status_code)
print(response.text)
