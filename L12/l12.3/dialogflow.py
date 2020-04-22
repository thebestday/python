import apiai
import json

token = '34c4bd4faac64e7f847466debaba441c'
# оформим все виде функци
# на вход подается месседж
def bot_answer(message):
    # создавать объект который будет отправлять запросы к боту и получать ответы
    # объект этот в apiai называется он с большой буквы ApiAI(token) и воспользоватьеся методом text_request()
    # так мы создадим объект подключения по этому токену к чат-боту
    request = apiai.ApiAI(token).text_request()
    # теперь сделаем настройку что будет язык русский( по умолчанию стоит анг)
    request.lang = 'ru'
    # теперь мы должны передать сообщение боту с помощью метода query - это и есть как раз запрос
    request.query = message
    # далее мы должны считать ответ в переменную responseJson - подгрузим ответ через модуль json.loads(request.getresponse()) ответ приходит в объект request метод getresponse
    # мы должны его прочитать .read() и если стоит кодировка какая то другая то перекинуть все в utf-8
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    # print(responseJson)   # 'fulfillment': {'speech': 'Привет!',
    response = responseJson['result']['fulfillment']['speech']
    return response

# дальше нам нужен нектороый мессендж от пользователя
message = ''
while(message != 'стоп'):
    message = input('Введите сообщение:')
    print(bot_answer(message))



