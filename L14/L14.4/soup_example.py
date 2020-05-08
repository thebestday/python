from bs4 import BeautifulSoup
import requests
import re
# from requsts.auth import HTTPBasicAuth, HTTPDigestAuth
# HTML документ представляет из себя иерархию некоторых областей - эти области задаются с помощью тегов div
# по классу будет осуществляться поиск области
# у класса main_center есть дети - все дивы которые вложены в этот центральный класс это его дети
# Beautifulsoup  имеет возможность считывать эту иерархию - он может показыать все вложенные состовляющие(классы, дивы, ...)
# фактически это дерево -граф -где можно наблюдать все вложения
# BS может осуществлять поиск не только по названию тега a/title/div а может осуществляться по классу
# допустим в данном классе лежит полезная нам информация - мы можем считать все объекты данного класса и можем опускаться на уровень ниже
# на том месте где нужно просмотреть код нажимаем и смотрим на класс
# при парсинге сайта встречается такая ситуация когда определенная информация доступна только  зарегеистрированым пользователям
# используют методы авторизации(регистрация зараннее) - необходимо авторизоваться-обычная процедура ввода логина и пароля
# для этого необходимо отправить специальный запрос - мы указываем в этом запросе параметры авторизации
#  указываем специальный параметр auth = HTTPBasicAuth
# response = requests.get('url', auth = HTTPBasicAuth('your_login', 'your_password'))
# после запроса можем получать контент который доступен авторизованному пользователю
URL = 'https://www.drom.ru/reviews/volvo/v40/5kopeek/'
page = requests.get(URL)
print(page.status_code)
# print(page.text)
soup = BeautifulSoup(page.text, "html.parser")
# ищем наш див
reviews = soup.find_all('div', class_ = 'b-fix-wordwrap')
print(len(reviews))
# поиск тегов по классу
rev_plus = []
rev_minus = []
i = 0
for rev in reviews:
    if i%3 == 0:
        rev_plus.append(rev.text)
        i+=1
    elif i%3 == 1:
        rev_minus.append(rev.text)
        i+=1
    else:
        i+=1
# print(rev_minus)

# иерархия
# старший класс b-wraper - создадим часть htmt элемента и найдем див class_ = 'b-wrapper'
# данный див можем найти с помощью атрибута contents - здесь будут записаны все составляющие этой части
parts = soup.find('div', class_ = 'b-wrapper')
print('************')
print(len(parts.contents))
for part in parts.contents:
    print('-----------------------------')
    print(part)
    # можем узнать сколько детей у класса b-wrapper
    try:
        print(len(part.contents))
    except:
        print('Error')
# те. contents это метод навигации по ирархии html документа
print("------------ANOTHER EXAMPLE")

URL_ ='https://auto.ria.com/reviews/volvo/v40/'

page_  = requests.get(URL_)
print(page_.status_code)
# так же создаем суп
soup_ = BeautifulSoup(page_.text, 'html.parser')
reviews_ = soup_.find_all('div', class_='reviews-car-cardi-top')
rev_ = []
for rev in reviews_:
    print(rev.text)
    rev_.append(rev)

print(rev_)
