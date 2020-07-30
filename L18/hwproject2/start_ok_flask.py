from flask import Flask, request, render_template
import requests
from average_wage import sallaryfunction
import sqlite3 as lite
import sys

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def hello():
    return render_template('main.html')


@app.route('/contacts')
def contact():
    return render_template('contacts.html')


@app.route('/new_data', methods=['POST', 'GET'])
def search_form2():
    spec = request.form['specialisation']
    sallary = request.form['sallary']
    location = request.form['location']
    work_place = request.form['work_place']
    comment =  request.form['comment']
    commentcity = request.form['commentcity']

    if comment != '':
        spec = comment

    if commentcity != '':
        location = commentcity


    mid_sal_from, mid_sal_to, all_found  = sallaryfunction(sallary, spec, location)

    data = {
        'spec': spec,
        'sallary': sallary,
        'location': location,
        'work_place': work_place,
        'comment': comment,
        'commentcity': commentcity,
        'mid_sal_from': mid_sal_from,
        'mid_sal_to': mid_sal_to,
        'all_found': all_found
    }

    print("зарплата {}-разработчика в {} для выбранной зарплаты от {} составляет в среднем  от {}руб. до {}руб.".format(spec, location, sallary, mid_sal_from, mid_sal_to))
    # print(work_place, type(work_place))


    print('-----------DB---------------')
    connect = None
    try:
        connect = lite.connect('startok.db')
        cur = connect.cursor()
        cur.execute('SELECT SQLITE_VERSION()')
        # берем первый объект из полученных данных и помещяем его в переменную data
        datadb = cur.fetchone()[0]
        print(f'SQLite version: {datadb}')           # SQLite version: 3.31.1
    except lite.Error as e:
        print(f'Error {e.args[0]}:')
        sys.exit()
    # что бы создать таблицу - необходимо выполнит такой sql запрос поэтому закоментируем код создания таблицы


    if ('SELECT * from cities LIMIT 1') == True:
        sqlite_select_query = """SELECT * from cities"""
        cur.execute(sqlite_select_query)
        records = cur.fetchall()

        with connect:
            cur.execute("SELECT Count() FROM cities")
            id = cur.fetchone()[0]
            cur.execute("INSERT INTO cities VALUES(?,?,?,?,?,?,?,?,?)", (id+1, f'{spec}', f'{sallary}', f'{location}', f'{comment}', f'{commentcity}', mid_sal_from, mid_sal_to, all_found))
            connect.commit()

        for row in records:
            print(row)

        print(len(records))
        print(f'rows updated: {cur.rowcount}')

        connect.close()

    if ('SELECT * from cities LIMIT 1') == False:
        cur.execute('CREATE TABLE cities(id INT, spec TEXT, sallary TEXT, location TEXT, comment TEXT, commentcity TEXT, mid_sal_from INT, mid_sal_to INT, all_found INT)')

    return render_template('new_data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
