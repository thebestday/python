from flask import Flask, request, render_template
import requests
from average_wage import sallaryfunction
import sqlite3 as lite
import sys
from sqlalchemy import Column, Integer, String, Float, create_engine, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import class_mapper


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
    comment =  request.form['comment']
    commentcity = request.form['commentcity']
    work_place = request.form.get('check')

    if work_place == None:
        work_place = 'No'
    if comment != '':
        spec = comment

    if commentcity != '':
        location = commentcity

    def get_work_place():
        return work_place

    mid_sal_from, mid_sal_to, all_found, salary_USD = sallaryfunction(sallary, spec, location, work_place)

    data = {
        'id': id,
        'spec': spec,
        'sallary': sallary,
        'location': location,
        'work_place': work_place,
        'comment': comment,
        'commentcity': commentcity,
        'mid_sal_from': mid_sal_from,
        'mid_sal_to': mid_sal_to,
        'all_found': all_found,
        'salary_USD': salary_USD
    }

    print(work_place, type(work_place))
    print(salary_USD, type(salary_USD))

    print("зарплата {}-разработчика в {} для выбранной зарплаты от {} составляет в среднем  от {}руб. до {}руб.".format(spec, location, sallary, mid_sal_from, mid_sal_to))



    print('-----------DB---------------')
    # создаем движок -фактичекм подключение к бд(если бызы нет то она создаться(адрес - то что после /// - можно указать путь к папке)
    # echo = True будем видеть какие sql запросы отправляются в БД- будем вызывать в действительности методы а видеть запросы
    engine = create_engine('sqlite:///orm1.sqlite', echo=False)
    # используем декларативный способ связи с базой данных(будем зараннее создавать класс(который наслудуется от класса Base))
    # и под этот класс будет впоследствии создана таблица в БД(это и есть декларативный способ)
    Base = declarative_base()

    class HH_request(Base):
        # задаем имя таблицы
        __tablename__ = 'HH_DATA'
        # создаем первичный ключ
        id = Column(Integer, primary_key=True)
        spec = Column(String)
        sallary = Column(Integer)
        location = Column(String)
        work_place = Column(String)
        comment = Column(String)
        commentcity = Column(String)
        mid_sal_from = Column(Integer)
        mid_sal_to = Column(Integer)
        all_found = Column(String)
        salary_USD = Column(Integer)


        # id-ник не указываем потому что он автоматически присваивается объекту
        def __init__(self, spec, sallary, location, work_place, comment, commentcity, mid_sal_from, mid_sal_to, all_found, salary_USD):
            self.spec = spec
            self.sallary = sallary
            self.location = location
            self.work_place = work_place
            self.comment = comment
            self.commentcity = commentcity
            self.mid_sal_from = mid_sal_from
            self.mid_sal_to = mid_sal_to
            self.all_found = all_found
            self.salary_USD = salary_USD


        def __str__(self):
            return f'{self.id}, {self.spec}, {self.sallary}, {self.location}, {self.work_place}, {self.comment}, {self.commentcity}, {self.mid_sal_from}, {self.mid_sal_to}, {self.all_found}, {self.salary_USD}'

        def __repr__(self):
            return {self.id}

    # ok класс готов теперь можно запускать
# для этого необходимо вызавать у объекта Base метод metadata и create_all() - при этом будет создана таблица которая соответсвует данному классу
    Base.metadata.create_all(engine)
    # все действия происходит с базами данных  в сессиях
    # пока только создаем объект сессии sessionmaker и указать в качестве параметра bind=engine  т.е тот движок который мы определи выше
    Session = sessionmaker(bind=engine)
    # теперь опеределяем сессию (теперь можем в этой сессии общаться с базой данных)
    session = Session()
    HH_request_1 = HH_request(spec, sallary, location, work_place, comment, commentcity, mid_sal_from, mid_sal_to, all_found, salary_USD)
    session.add(HH_request_1)
    session.commit()
    hh_all = session.query(HH_request)

    # hhIDISHNIK = list(HH_request.__table__.primary_key)
    # print(hhIDISHNIK[0])


    for hh in hh_all:
        print(hh)
        print(hh.id)

    hhspec = session.query(spec)
    print(hhspec)

    data['id'] = HH_request_1.id

    id_all = []
    idall = HH_request_1.id
    id_all.append(idall)
    print(id_all)


    # dishnik = [pk.name for pk in HH_request.__table__.primary_key]
    # print(dishnik)
    # hhid = inspect(HH_request).primary_key[0]                                           # HH_DATA.id
    # print(hhid)
    # hhID = [key.name for key in inspect(HH_request).primary_key]                           # ['id']
    # print(hhID)
    # HHID = class_mapper(HH_request).primary_key[0]                                       # HH_DATA.id
    # print(HHID)
    # IDHH = HH_request.__mapper__.primary_key         #(Column('id', Integer(), table=<HH_DATA>, primary_key=True, nullable=False),)
    # print(IDHH[0])                                     # HH_DATA.id

    return render_template('new_data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)

