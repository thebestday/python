import requests
import pprint

SERVER = 'http://127.0.0.1:5000/'
DIR = 'example'


# ЗАПРОС-ТЕСТ
result = requests.get(SERVER)
print(result.status_code, result.text)

# POST
headers = {'Content-Type': 'application/json'}

(key, val) = ('mode', 2)
result = requests.post(f'{SERVER}api/{DIR}/{key}',
    headers=headers,
    data='{"%s":"%s"}' % (key, val)
)
print(result.status_code)

# get
result = requests.get(f'{SERVER}api/{DIR}/{key}')
print(result.status_code, result.text)