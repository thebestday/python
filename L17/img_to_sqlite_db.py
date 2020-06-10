import _sqlite3 as lite
import sys
import requests


response = requests.get('https://www.freeimages.com/') #url is definitely correct
picture = lite.Binary(response.content)
con = lite.connect('db_filename')
cursor = con.cursor()
sql = '''CREATE TABLE member_data(id integer primary key autoincrement, picture BLOB, name TEXT);'''
cursor.execute(sql)
# sql = '''INSERT INTO member_data (picture, name) VALUES ("{}", "{}",)'''.format(photo, member_name)
# cursor.execute(sql)
sql = '''INSERT INTO member_data (picture, name) VALUES (?, ?)'''
cursor.execute(sql, (photo, member_name))
con.commit()

