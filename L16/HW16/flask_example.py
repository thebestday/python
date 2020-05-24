from flask import Flask, request, render_template
from average_wage import *

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def hello():
    return render_template('main.html')

spec = ''
sallary = ''
location = ''
work_place = ''

@app.route('/search', methods = ['POST'])
def search_form():
    spec = request.form['specialisation']
    sallary = request.form['sallary']
    location = request.form['location']
    work_place = request.form['work_place']
    data = {
        'spec': spec,
        'sallary': sallary,
        'location': location,
        'work_place': work_place,
        'mid_sal_from': mid_sal_from,
        'mid_sal_to': mid_sal_to
    }
    return render_template('search.html', data=data)




@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == "__main__":
    app.run(debug=True)



