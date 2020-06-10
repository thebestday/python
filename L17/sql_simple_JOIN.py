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

# cur.execute("INSERT INTO cars VALUES(?,?,?)", (1, 'Audu', 234212))
# cur.execute("INSERT INTO cars VALUES(2, 'Mercedes', 57127)")
# cur.execute("INSERT INTO cars VALUES(3, 'Scoda', 9000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Bentley', 350000)")
# cur.execute("INSERT INTO cars VALUES(6, 'Citroen', 21000)")
# cur.execute("INSERT INTO cars VALUES(7, 'Hummer', 414000)")
# cur.execute("INSERT INTO cars VALUES(8, 'Volkswagen', 21600)")

# Добавим данные для этого создадим список

# cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]
#
# for car in cars_list:
#     cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0], car[1], car[2]))



# Сделаем еще одну таблицу - год машины - будет состоять из марки и года
# cur.execute("CREATE TABLE cars_year(name TEXT, year INT)")
cur.execute("INSERT INTO cars_year VALUES('Volvo', 2018)")
cur.execute("INSERT INTO cars_year VALUES('Bently', 2011)")
cur.execute("INSERT INTO cars_year VALUES('Citroen', 1937)")
cur.execute("INSERT INTO cars_year VALUES('LADA', 1945)")

# ТЕПЕРЬ МЫ ХОТИМ ПОЛУЧИТЬ ОБЩУЮ ТАБЛИЦУ СОСТОЯЩУЮ ИЗ марка год стоимость
# ДЕЛАЕМ ЭТО  СПОМОЩЬЮ ОПЕРАЦИИ join
with connect:

    cur = connect.cursor()
    # присоединяем по именам - столбец name
    # автоматически находится совпадение по именам и соединяются те строки где имена ОДИНАКОВЫЕ
    rows_join= f"SELECT * FROM cars JOIN cars_year ON cars.name = cars_year.name"
    #rows_join= f"SELECT * FROM cars INNER JOIN cars_year ON cars.name = cars_year.name"
    # rows_join = f"SELECT * FROM cars LEFT JOIN cars_year ON cars.name = cars_year.name"
    #rows_join = f"SELECT * FROM cars RIGHT JOIN cars_year ON cars.name = cars_year.name"
    cur.execute(rows_join)
    rows = cur.fetchall()
    for row in rows:
        print(row)


# теперь можем посмотреть что у нас в база
# sqlite_select_query = """SELECT * from cars"""
# cur.execute(sqlite_select_query)
# records = cur.fetchall()
# print(len(records))
# for row in records:
#     print((row))

# Закрываем сессию с базой
connect.close()