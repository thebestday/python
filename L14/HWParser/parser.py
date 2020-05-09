import requests
from bs4 import BeautifulSoup
import csv
import re

# URL = 'https://auto.ria.com/newauto/marka-jeep/?page=4&markaId=32'
URL = "https://auto.ria.com/newauto/marka-jeep/"
# ЧТО БЫ СЕРВИС НА ПОСЧИТАЛ БОТОМ воспользуемся заголовками(имитровать работу браузера)
HEADERS = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'accept': '*/*'}
HOST = 'https://auto.ria.com'
FILE = 'cars.csv'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find_all('span', class_='mhide')
    if pages:
        return int(pages[-1].get_text())
    else:
        return 1
    # print(pages, len(pages), "-------------pages")

# ф-я принимает html  с которым будет работать
pattern = r'https?://[\S]+'
def get_content(html):
# что бы парсить html создаем объект soup - вторым параметром передаем в конструктор тип документа (библиотека работает не только с html, xml)
# создали объект
    soup = BeautifulSoup(html, 'html.parser')         # создали объект
# find_all позволяет получить колекцию элементов
    items = soup.find_all('div', class_ = 'proposition')
    # print(items, type(items))
    print('--------------------')
    print('--------------------')
    cars = []
    for item in items:
        # проверим есть ли цена
        price_usd = item.find('span', class_='green bold size18')
        if price_usd:
            usd_price = price_usd.get_text(strip=True)
            # usd_price = price_usd.get_text(strip=True).replace(' $', '')
        else:
            usd_price = 'Цена не указана'
        cars.append({
            # 'title1': item.find('h3', class_='proposition_name').get_text(strip=True),
            # 'title2': item.find('div', class_='proposition_equip').get_text(strip=True),
            # 'title': item.find('h3', class_='proposition_name').text + ' ' + item.find('div', class_='proposition_equip').text
            'title': item.find('h3', class_='proposition_name').get_text(strip=True) + ' ' +  item.find('div', class_='proposition_equip').get_text(strip=True),
            'link': HOST + item.find('a').get('href'),
            'usd_price': usd_price,
            'fuel': item.find('span', class_='i-block').get_text(),
            # 'fuel': item.find('span', class_='size13').get_text()
            'volume': item.find('span', class_='i-block').find_next('span').get_text()
        })
    print(cars, len(cars))
    return cars

# сохраняем в файл
def save(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена $', 'Топливо', 'Объем двигателя'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['usd_price'], item['fuel'], item['volume']])



def parse():
    # URL = input('Enter URL: ')
    # URL = URL.strip()
    html = get_html(URL)
    print(html)             # <Response [200]>
    print(html.status_code)  # 200
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг старицы {page} из {pages_count}')
            html = get_html(URL, params={'page': page})
            cars.extend(get_content(html.text))
            print('-----------------------------------------------')
        # print(cars)
        save(cars, FILE)

        print(f'Получено {len(cars)} автомобилей')
        # что бы получить контент страницы нужно обратиться к свойству content или text
        # print(html.content)
        # print(html.text)               # получили html код страницы к которой обращаемся
        # cars = get_content(html.text)
    else:
        print('Error')

parse()