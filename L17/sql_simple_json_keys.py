import _sqlite3 as lite
import sys


connect = None

try:
    connect = lite.connect('test.db')
    cur = connect.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()[0]
    print(f'SQLite version: {data}')           # SQLite version: 3.31.1
except lite.Error as e:
    print(f'Error {e.args[0]}:')
    sys.exit()


# поэтому закоментируем код создания таблицы
# cur.execute('CREATE TABLE cars(id INT, name TEXT, price INT)')

cur.execute("INSERT INTO cars VALUES(?,?,?)", (1, 'Audu', 234212))
cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
cur.execute("INSERT INTO cars VALUES(3, 'Scoda', 9000)")
cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
cur.execute("INSERT INTO cars VALUES(5, 'Bentley', 350000)")
cur.execute("INSERT INTO cars VALUES(6, 'Citroen', 21000)")
cur.execute("INSERT INTO cars VALUES(7, 'Hummer', 414000)")
cur.execute("INSERT INTO cars VALUES(8, 'Volkswagen', 21600)")


cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]

for car in cars_list:
    cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0], car[1], car[2]))

# # теперь можем посмотреть что у нас в база
# sqlite_select_query = """SELECT * from cars"""
# cur.execute(sqlite_select_query)
# # когда мы получаем fetchall мы ПОЛУЧАЕМ КОРТЕЖИ ( кортеж кортежей)
# records = cur.fetchall()
# print(len(records))
# for row in records:
#     print((row))

# когда мы получаем fetchall мы ПОЛУЧАЕМ КОРТЕЖИ ( кортеж кортежей) иногда это удобно а бывает что удобнее работать с JSON
# т.е оперировать ключами
# ЭТО ДЕЛАЕТСЯ С ПОМОЩЬЮ СПЕЦИАЛЬНОЙ НАСТРОЙКИ -МЫ НАСТРАИВАЕМ атрибут .row-factory = lite.Row
# в таком случае у нас будут возращаться JSON причем ключами у нас будут именно колонок
with connect:
    connect.row_factory = lite.Row
    cur = connect.cursor()
    cur.execute("SELECT * FROM cars")
    rows = cur.fetchall()           # выгружаем базу в память

    for row in rows:
        # выводим обращаясь к row как к дикту
        print(f"{row['id']}, {row['name']}, {row['price']}")


# Закрываем сессию с базой
connect.close()