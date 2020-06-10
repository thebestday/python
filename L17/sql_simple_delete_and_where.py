import _sqlite3 as lite
import sys

connect = None

try:
    connect = lite.connect('test2.db')
    cur = connect.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()[0]
    print(f'SQLite version: {data}')           # SQLite version: 3.31.1
except lite.Error as e:
    print(f'Error {e.args[0]}:')
    sys.exit()

# поэтому закоментируем код создания таблицы
# cur.execute('CREATE TABLE cars2(id INT, name TEXT, price INT)')

# cur.execute("INSERT INTO cars2 VALUES(?,?,?)", (1, 'Audu', 234212))
# cur.execute("INSERT INTO cars2 VALUES(2, 'Mercedes', 57127)")
# cur.execute("INSERT INTO cars2 VALUES(3, 'Scoda', 9000)")
# cur.execute("INSERT INTO cars2 VALUES(4, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars2 VALUES(5, 'Bentley', 350000)")
# cur.execute("INSERT INTO cars2 VALUES(6, 'Citroen', 21000)")
# cur.execute("INSERT INTO cars2 VALUES(7, 'Hummer', 414000)")
# cur.execute("INSERT INTO cars2 VALUES(8, 'Volkswagen', 21600)")
#
connect.commit()
# Добавим данные для этого создадим список

# cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]
#
# for car in cars_list:
#     cur.execute("INSERT INTO cars2 VALUES(?,?,?)", (car[0], car[1], car[2]))

connect.commit()
# Редактирование данных(DELETE and WHERE)
with connect:
    cur = connect.cursor()
    # uId = 2
    # cur.execute(f"DELETE FROM cars2 WHERE id={uId}")            # удаляем строки с id = 2
    # cur.execute("SELECT DISTINCT price FROM cars2 ORDER BY price")
    # cur.execute("DELETE FROM cars2 WHERE(SELECT DISTINCT id FROM cars2 ORDER BY id)")
    cur.execute("DELETE FROM cars2 WHERE id NOT IN( SELECT MIN(id) id FROM cars2 GROUP BY name, name)")
    print(f"NUmber of rows updated: {cur.rowcount}")

connect.commit()

sqlite_select_query = """SELECT * from cars2"""
cur.execute(sqlite_select_query)

records = cur.fetchall()
print(len(records))
for row in records:
    print((row))

# Закрываем сессию с базой
connect.close()