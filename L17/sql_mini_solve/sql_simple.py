import sqlite3 as lite
import sys
from flask_example import search_form
from flask_example import all_values
from average_wage import sallaryfunction


spec, sallary, location, comment, commentcity, mid_sal_from, mid_sal_to, all_found = search_form()
print(spec, sallary, location, comment, commentcity, mid_sal_from, mid_sal_to, all_found)
print(spec, type(spec))
print(sallary, type(sallary))
print(location, type(location))
print(comment, type(comment))
print(commentcity, type(commentcity))
print(mid_sal_from, type(mid_sal_from))
print(mid_sal_to, type(mid_sal_to))
print(all_found, type(all_found))

#
# connect = None
# try:
#     connect = lite.connect('test.db')
#     cur = connect.cursor()
#     cur.execute('SELECT SQLITE_VERSION()')
#     # берем первый объект из полученных данных и помещяем его в переменную data
#     data = cur.fetchone()[0]
#     print(f'SQLite version: {data}')           # SQLite version: 3.31.1
# except lite.Error as e:
#     print(f'Error {e.args[0]}:')
#     sys.exit()
#
#
# # что бы создать таблицу - необходимо выполнит такой sql запрос
# # CREATE TABLE далее идет название таблицы cars и далее перечесляем название и типы строк( INT, TEXT)
# # поэтому закоментируем код создания таблицы
# cur.execute('CREATE TABLE cities(id INT, spec TEXT, sallary TEXT, location TEXT, comment TEXT, commentcity TEXT, mid_sal_from INT, mid_sal_to INT, all_found INT)')
#
# # ДОБАВЛЕНИЕ ДАННЫХ В ТАБЛИЦУ
# # INSERT КУДА INTO в таблицу cars значение
# # 1 СПОСОБ С ЯВНЫМ ПРОПИСЫВАНИЕМ ДАННЫХ VALUES(2, 'Mercedes', 57127) когда их немного и мы можем их руками забить
# # 2 СПОСОБ - полуавтоматический ...VALUES(?,?,?)", (1, 'Audi', 234212) - мы можем в цикле записать из какого-то словаря значения в базу
#
# cur.execute("INSERT INTO cities VALUES(?,?,?)", (1, 'Audu', 234212))
# cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
# cur.execute("INSERT INTO cars VALUES(3, 'Scoda', 9000)")
#
#
# # Добавим данные для этого создадим список
#
# cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]
#
# for car in cars_list:
#     cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0], car[1], car[2]))
#
# # теперь можем посмотреть что у нас в база
# # Выгружаем данные полностью  *
# # создаем запрос на выгрузку всех данных из базы ( или можем указать конкретные колонки)
# sqlite_select_query = """SELECT * from cars"""
# cur.execute(sqlite_select_query)
# # fetchall забирает полностью вернувшийся объект (fetchone забирает только первый объект)
# # но есть вероятность переполнения оперативной памяти если  большой объем данных вернулся из базы
# # когда мы получаем fetchall мы ПОЛУЧАЕМ КОРТЕЖИ ( кортеж кортежей)
# records = cur.fetchall()
# print(len(records))
# for row in records:
#     print((row))
#
# # Закрываем сессию с базой
# connect.close()
#



#
# print(spec, type(spec))
# print(sallary, type(sallary))
# print(location, type(location))
# print(comment, type(comment))
# print(commentcity, type(commentcity))
# print(mid_sal_from, type(mid_sal_from))
# print(mid_sal_to, type(mid_sal_to))
# print(all_found, type(all_found))
