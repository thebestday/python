from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///orm.sqlite', echo=True)

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key = True)
    model = Column(String)
    price = Column(Float)
    city = Column(String)

    def __init__(self, model, price, city):
        self.model = model
        self.price = price
        self.city = city

    def __str__(self):
       return f'{self.id}, {self.model}, {self.price}, {self.city}'

# класс готов - можно запускать- для этого необходимо вызвать у обьекта Base метод metadata.create_all()
# будет создана таблица которая соотвествует данному классу
Base.metadata.create_all(engine)
# все действия происходят с бд в сессиях - для этого создаем объект Session
# и указать в качестве параметра bind = engine тот движок который мы определили выше
Session = sessionmaker(bind = engine)
# определим сессию
session = Session()

# ок таблица создалась - теперь насытим ее данными
car_1 = Car('Volvo', 1.2, 'Moscow')
car_2 = Car('BMW', 1.6, 'Kazan')
car_3 = Car('Lada', 0.5, 'Moscow')
car_4 = Car('AUDI', 2.6, 'Kazan')
# вызываем метод add у объекта сессии что бы добавить наши объекты
session.add(car_1)
session.add(car_2)
session.add(car_3)
session.add(car_4)

# что бы изменения каснулить данной таблицы необходимо сдлеть коммит
session.commit()

# делаем запрос с помощью метода query
cars_query = session.query(Car)

print(type(cars_query))

for car in cars_query:
    print(car, type(car))