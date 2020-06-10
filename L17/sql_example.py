import random
import sqlite3 as lite
import sys

NUM_EMP = 50
NUM_DEP = 5
NAME_EMP = 'Natalia Ksenia Viola Ivan Kostya Kosmos Katya Darya Valya Nikita Serezha Vitya Sarah Petya Victor Seva Lyonya Maxim Vova Raya'.split()

# Подключаемся к базе (создаем базу)
connect = None

try:
    connect = lite.connect('testotdel.db')
    cur = connect.cursor()
except lite.Error as e:
    print(f"Error {e.args[0]}:")
    sys.exit(1)

# создадим таблицу
# cur.execute("CREATE TABLE staff(id INT,id_dep INT, id_head INT, name TEXT, sal INT)")

# наполняем данными
# '''
# для простоты будем считать, что в каждом департаменте один руководитель.
# У 1-го департамента - сотрудник с id = 1, у 2-го с id = 2, ...
# '''
# for i in range(1, NUM_EMP + 1):
#     id_dep = random.randint(1, NUM_DEP)
#     cur.execute("INSERT INTO staff VALUES(?,?,?,?,?)",
#                 (i, id_dep, id_dep, NAME_EMP[random.randint(0, len(NAME_EMP) - 1)], random.randint(10000, 50000)))
# # поправим недораузуменее, что у руководителей департаментов сейчас стоят случайные департаменты
# for i in range(1, 6):
#     cur.execute("UPDATE staff SET id_dep=?, id_head = ? WHERE id=?", (i, i, i))
#
# connect.commit()

# посмотрим, что получилось
sqlite_select_query = """SELECT *from staff"""
cur.execute(sqlite_select_query)

records = cur.fetchall()

for row in records:
    print(row)

# '''
# Вывести отдел с наибольшим числом сотрудников.
# '''
#
query_otd = """SELECT id_dep, COUNT(id_dep)as Result from staff GROUP BY id_dep """
cur.execute(query_otd)
recordsotd = cur.fetchall()
for i in range(len(recordsotd)):
    print(f'В отделе {recordsotd[i][0]} число сотрудников: {recordsotd[i][1]}')
for row in recordsotd:
    print(row)


query = """SELECT id_dep, COUNT(id_dep)as Result from staff GROUP BY id_dep ORDER BY Result DESC limit 1"""
cur.execute(query)
records = cur.fetchone()
print(f'В отделе {records[0]} наибольшее число сотрудников: {records[1]}')

# '''
# Вывести список сотрудников, получающих заработную плату выше, чем у руководителя.
# '''
#
query = f"SELECT COUNT(*) from (SELECT t1.id, t1.sal, t2.sal as sal_head FROM staff t1 JOIN staff t2 ON t1.id_head = t2.id) as T where T.sal>T.sal_head"
cur.execute(query)
records = cur.fetchone()
print(f'Таких негодяев {records[0]}')


# f"DELETE FROM staff WHERE id IN(SELECT id={id})"