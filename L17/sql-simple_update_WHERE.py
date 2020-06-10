import _sqlite3 as lite
import sys

connect = None
# с помощью модели try accept попробуем подключиться к базе
# если бызы test.db нет в директории - то sqlite ее создаст
try:
    connect = lite.connect('test1.db')
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

# поэтому закоментируем код создания таблицы
# cur.execute('CREATE TABLE cars1(id INT, name TEXT, price INT)')


cur.execute("INSERT INTO cars1 VALUES(?,?,?)", (1, 'Audu', 234212))
cur.execute("INSERT INTO cars1 VALUES(2, 'Mercedes', 57127)")
cur.execute("INSERT INTO cars1 VALUES(3, 'Scoda', 9000)")
cur.execute("INSERT INTO cars1 VALUES(4, 'Volvo', 29000)")
cur.execute("INSERT INTO cars1 VALUES(5, 'Bentley', 350000)")
cur.execute("INSERT INTO cars1 VALUES(6, 'Citroen', 21000)")
cur.execute("INSERT INTO cars1 VALUES(7, 'Hummer', 414000)")
cur.execute("INSERT INTO cars1 VALUES(8, 'Volkswagen', 21600)")

# Добавим данные для этого создадим список

cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]

for car in cars_list:
    cur.execute("INSERT INTO cars1 VALUES(?,?,?)", (car[0], car[1], car[2]))

# методы UPDATE И WHERE- условие по которому можем отсеивать что-то
with connect:
    cur = connect.cursor()
    uPrice = 100
    uId = 2
    cur.execute("UPDATE cars1 SET price=? WHERE id>?", (uPrice, uId))
    print(f"Number of rows updated: {cur.rowcount}")

sqlite_select_query = """SELECT * from cars1"""
cur.execute(sqlite_select_query)
records = cur.fetchall()
print(len(records))
for row in records:
    print((row))




# Закрываем сессию с базой
connect.close()
