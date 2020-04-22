import requests
import pprint

URL = 'https://api.hh.ru/vacancies'
# Делаем запрос - узнаем количество вакансий где требуются навыки разработки на языке Python
# для этого создаем словарь с ключом text: Python что бы вернуло первую страницу по запросу Python
# params = {'text': "Python",
#           'page': 1}
#
# result = requests.get(URL, params=params).json()
# # ВЫВЕДЕМ РЕЗУЛЬТАТ
# pprint.pprint(result)
# # ВЫВЕДЕМ РЕЗУЛЬТАТ колчиство - ЭТОГО ОБРАТИМСЯ по ключу result['found']
# # print(dir(result))
# pprint.pprint(result['found'])

# Сделаем более сложный запрос
# хотим найти разработчиков Python в какой- то конретной компании - для этого напишем новый params
params = {'text': 'NAME:(Python OR C++) AND (MAIL OR YANDEX)'}
result = requests.get(URL, params = params).json()
# pprint.pprint(result['found'])
pprint.pprint(result['items'])


