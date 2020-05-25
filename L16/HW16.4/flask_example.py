from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/main')
def hello():
    return render_template('main.html')


@app.route('/search', methods = ['POST'])
def search_form():
    spec= request.form['specialisation']
    sallary = request.form['sallary']
    location = request.form['location']
    work_place = request.form['work_place']
    # print(int(sallary), type(int(sallary)))
    URL = 'https://api.hh.ru/vacancies'

    params = {'text': '{} AND {}'.format(spec, location),
              'only_with_salary': True,
              'page': 1,
              'per_page': 20}

    result = requests.get(URL, params=params).json()
    all_found = result['found']
    pages = result['pages']
    print('все вакансии {} на {} страницах'.format(all_found, pages))

    salary_from = []
    salary_to = []

    for i in range(1, pages):
        URL = 'https://api.hh.ru/vacancies'
        params = {'text': 'Python AND Moscow',
                  'only_with_salary': True,
                  'page': i,
                  'per_page': 20}
        result = requests.get(URL, params=params).json()
        items = result['items']

        for i in items:
            salary = i['salary']
            # print(salary, type(salary))
            sal_from = salary['from']
            # print(sal_from, type(sal_from))
            sal_to = salary['to']
            # if sal_from >= int(sallary):
            if sal_from != None: salary_from.append(sal_from)
            if sal_to != None: salary_to.append(sal_to)

    mid_sal_from = round(sum(salary_from) / len(salary_from))
    mid_sal_to = round(sum(salary_to) / len(salary_to))


    data = {
        'spec': spec,
        'sallary': sallary,
        'location': location,
        'work_place': work_place,
        'mid_sal_from': mid_sal_from,
        'mid_sal_to': mid_sal_to,
        'all_found': all_found

    }
    # print(f"зарплата Pyton-разработчика  составляет в среднем  от {mid_sal_from}руб. до {mid_sal_to}руб.")
    # print ("зарплата {}-разработчика в {} составляет в среднем  от {}руб. до {}руб.".format(spec, location, mid_sal_from, mid_sal_to ))
    print ("зарплата {}-разработчика в {} для выбранной зарплаты от {} составляет в среднем  от {}руб. до {}руб.".format(spec, location, sallary, mid_sal_from, mid_sal_to ))

    return render_template('search.html', data=data)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')




if __name__ == "__main__":
    app.run(debug=True)



