from flask import Flask, request, render_template
import requests
from average_wage import sallaryfunction

app = Flask(__name__)


@app.route('/')
@app.route('/main')
def hello():
    return render_template('main.html')


@app.route('/contacts')
def contact():
    return render_template('contacts.html')


@app.route('/search', methods=['POST', 'GET'])
def search_form():
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

    mid_sal_from= sallaryfunction(sallary, spec, location)[0]
    mid_sal_to = sallaryfunction(sallary, spec, location)[1]
    all_found = sallaryfunction(sallary, spec, location)[2]

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

    return render_template('search.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
