import _sqlite3 as lite
import sys
# pip install pysqlite3         устнавливаем пакет
# в памяти один файл - ни каких серверов не нужно - поэтому удобно тестировать код и реальзовывать простые проекты

connect = None
# с помощью модели try accept попробуем подключиться к базе
# если бызы test.db нет в директории - то sqlite ее создаст
try:
    connect = lite.connect('test.db')
    # устанавливаем курсор- каретка которая ходит по базе и имеет какое-то положение постоянно
    # с помощью курсора мы можем осуществлять навигацию по  данным которые мы запросили изи базы данных
    cur = connect.cursor()
    # посмотрим на версию sqlite
    cur.execute('SELECT SQLITE_VERSION()')
    # с помощью метода fetchone - получаем из курсора те данные- которые курсор получил по запросу
    # берем первый объект из полученных данных и помещяем его в переменную data
    data = cur.fetchone()[0]
    print(f'SQLite version: {data}')           # SQLite version: 3.31.1
except lite.Error as e:
    print(f'Error {e.args[0]}:')
    sys.exit()

# Создаем таблицу ( используем базу с машинами)
# первый стобец - это будет первичный ключ
# второй стобец - это будет марка автомобиля
# третий столбец - это стоимость авто

# что бы создать таблицу - необходимо выполнит такой sql запрос
# CREATE TABLE далее идет название таблицы cars и далее перечесляем название и типы строк( INT, TEXT)
# ЕСЛИ ПОСЛЕ СОЗДАНИЯ ПОПЫТАТЬСЯ СНОВА СОЗДАТЬ ТАБЛИЦИ ТО ВЫХОДИТ ошибка table cars already exists
# поэтому закоментируем код создания таблицы
# cur.execute('CREATE TABLE cars(id INT, name TEXT, price INT)')

# ДОБАВЛЕНИЕ ДАННЫХ В ТАБЛИЦУ
# INSERT КУДА INTO в таблицу cars значение
# 1 СПОСОБ С ЯВНЫМ ПРОПИСЫВАНИЕМ ДАННЫХ VALUES(2, 'Mercedes', 57127) когда их немного и мы можем их руками забить
# 2 СПОСОБ - полуавтоматический ...VALUES(?,?,?)", (1, 'Audi', 234212) - мы можем в цикле записать из какого-то словаря значения в базу

cur.execute("INSERT INTO cars VALUES(?,?,?)", (1, 'Audu', 234212))
cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
cur.execute("INSERT INTO cars VALUES(3, 'Scoda', 9000)")
cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
cur.execute("INSERT INTO cars VALUES(5, 'Bentley', 350000)")
cur.execute("INSERT INTO cars VALUES(6, 'Citroen', 21000)")
cur.execute("INSERT INTO cars VALUES(7, 'Hummer', 414000)")
cur.execute("INSERT INTO cars VALUES(8, 'Volkswagen', 21600)")

# Добавим данные для этого создадим список

cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]

for car in cars_list:
    cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0], car[1], car[2]))

# теперь можем посмотреть что у нас в база
# Выгружаем данные полностью  *
# создаем запрос на выгрузку всех данных из базы ( или можем указать конкретные колонки)
sqlite_select_query = """SELECT * from cars"""
cur.execute(sqlite_select_query)
# fetchall забирает полностью вернувшийся объект (fetchone забирает только первый объект)
# но есть вероятность переполнения оперативной памяти если  большой объем данных вернулся из базы
# когда мы получаем fetchall мы ПОЛУЧАЕМ КОРТЕЖИ ( кортеж кортежей)
records = cur.fetchall()
print(len(records))
for row in records:
    print((row))

# Закрываем сессию с базой
connect.close()