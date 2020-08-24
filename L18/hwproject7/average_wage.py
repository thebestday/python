
import requests
import pprint


# делаем первоначальный запрос для определения количеста вакансий  и количества страниц (переменные vacancies, pages)
def sallaryfunction(sallary, spec, location, work_place):
    URL = 'https://api.hh.ru/vacancies'

    if work_place == 'Yes':
        params = {'text': '{} AND {}'.format(spec, location),
                'only_with_salary': True,
                'page': 1,
                'per_page': 20,
                'schedule': 'remote'}
    else:
        params = {'text': '{} AND {}'.format(spec, location),
                  'only_with_salary': True,
                  'page': 1,
                  'per_page': 20}

    result = requests.get(URL, params=params).json()
    all_found = result['found']
    pages = result['pages']
    items = result['items']

    print('всего вакансий {} на {} страницах'. format(all_found, pages))
    print('-----работа функции sallaryfunction-----------------')

    salary_from = []
    salary_to =[]
    salary_USD = 0

    def pars_salary(currency):
        url_currency = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response_currency = requests.get(url_currency)
        result_json_currency = response_currency.json()
        if currency == 'USD':
            koefU = result_json_currency['Valute']['USD']['Value']
            return koefU
        if currency == 'EUR':
            koefE = result_json_currency['Valute']['EUR']['Value']
            return koefE

    print('-------------курсы валют--------------')
    print(pars_salary('USD'))
    print(pars_salary('EUR'))
    print('------------курсы валют----------------')
    for i in range(1, pages):
        for i in items:
            salary = i['salary']
            sal_from = salary['from']
            sal_to = salary['to']
            sal_cur = salary['currency']
            if isinstance(sal_from, int):
                if sal_cur == 'RUR':
                    if sal_from >= int(sallary):
                        if sal_from != None: salary_from.append(sal_from)
                        if sal_to != None: salary_to.append(sal_to)
                if sal_from != None and sal_to != None:
                    if sal_cur == 'USD':
                        salary_USD += 1
                        if (sal_from * pars_salary('USD')) >= int(sallary):
                            if sal_cur == 'USD': salary_from.append(sal_from * pars_salary('USD'))
                            if sal_cur == 'USD': salary_to.append(sal_to * pars_salary('USD'))
                            # print(f'Колич-во вакансий с заралатой в USD: {salary_USD}')
                # if sal_from != None and sal_to != None:
                #     if sal_cur == 'EUR':
                #         if (sal_from * pars_salary('EUR')) >= int(sallary):
                #             if sal_cur == 'EUR': salary_from.append(sal_from * pars_salary('EUR'))
                #             if sal_cur == 'EUR': salary_to.append(sal_to * pars_salary('EUR'))
                #             print(sal_from, pars_salary('EUR'), sal_from * pars_salary('EUR'))


            # print(sal_from, type(sal_from))
            # print(salary['currency'], type(salary['currency']))

            # if salary['currency'] == 'USD':
            #     koef = pars_salary('USD')
            # elif salary['currency'] == 'EUR':
            #     koef = pars_salary('EUR')
            # else:
            #     koef = 1
            # sal_from = koef * int(salary['from'])
            # sal_to = koef * int(salary['to'])

    salary_USD = int(salary_USD)
    mid_sal_from = round(sum(salary_from)/len(salary_from))
    mid_sal_to = round(sum(salary_to)/len(salary_to))
    # print ('зарплата Python-разработчика в Москве составляет в среднем  от {}руб. до {}руб.'.format(mid_sal_from, mid_sal_to ))
    return mid_sal_from, mid_sal_to, all_found, salary_USD









