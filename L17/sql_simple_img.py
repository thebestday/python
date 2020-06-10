import _sqlite3 as lite
import sys
connect = None
# Работа с изображение
def readImage(path):
    fin = None
    try:
        fin = open(path, "/")
        img = fin.read()
        return img
    except IOError as e:
        print(e)
        sys.exit(1)
    finally:
        if fin:
            fin.close()

with connect:
    cur = connect.cursor()
    img = readImage('python.png')
    img_binary = lite.Binary(img)
    id = 1
    cur.execute("CREATE TABLE images(id INT, data BLOB)")
    sqlite_insert_blob_query = """ INSERT INTO images (id, data) VALUES (?, ?)"""
    cur.execute(sqlite_insert_blob_query, (id, img_binary))

with connect:
    cur = connect.cursor()
    sqlite_select_query = """SELECT * from images"""
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    print(len(records))

    for row in records:
        print(row)

# Закрываем сессию с базой
connect.close()