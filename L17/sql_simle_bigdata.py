import _sqlite3 as lite
import sys

connect = None

try:
    connect = lite.connect('test.db')
    cur = connect.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()[0]
    print(f'SQLite version: {data}')
except lite.Error as e:
    print(f'Error {e.args[0]}:')
    sys.exit()


# ЕСЛИ ПОСЛЕ СОЗДАНИЯ ПОПЫТАТЬСЯ СНОВА СОЗДАТЬ ТАБЛИЦИ ТО ВЫХОДИТ ошибка table cars already exists
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

# Добавим данные для этого создадим список
cars_list = [[9, 'Lada', 5000], [10, 'Renault', 9000]]

for car in cars_list:
    cur.execute("INSERT INTO cars VALUES(?,?,?)", (car[0], car[1], car[2]))

# создаем запрос на выгрузку всех данных из базы ( или можем указать конкретные колонки)
sqlite_select_query = """SELECT * from cars"""
cur.execute(sqlite_select_query)
records = cur.fetchall()
print(len(records))
for row in records:
    print((row))

# Пример когда получаем большую выгрузку из базы и получать нужно поэлементно
# при большом объеме данных выгружать полностью бывает не целесообразно
# еще ОДИН СПОСОБ работы с базой это менеджер контекста или ключеовое слово with (забор строчек по одной)
with connect:
    cur = connect.cursor()
    cur.execute("SELECT * FROM cars")  # делаем полную выгрузку с базы
    while True:
        row = cur.fetchone() # считываем по одному элементу с курсора -курсоа каждый раз находиться на новой строчке( как каретка в текстовом файле)
        # он не хранит данные в памяти всю таблицу а считывает ее  по мере вызова функ-и fetchone()
        if row == None:
            break
        print(row[0], row[1], row[2])

# Закрываем сессию с базой
connect.close()