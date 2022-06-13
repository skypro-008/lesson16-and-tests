# Добавление городов
#
# Дана модель City и таблица city.
#
# Добавьте в базу данных сведения о городах
# в соответствии с таблицей ниже.
# +----+---------+------------+------------+
# | id |   name  | country_ru | population |
# +----+---------+------------+------------+
# | 1  |   Рим   |   Италия   |  28730000  |
# | 2  |  Милан  |   Италия   |  1333000   |
# | 3  | Венеция |   Италия   |   265000   |
# | 4  | Стамбул |   Турция   | 108950000  |
# | 5  |  Кемер  |   Турция   |   22421    |
# +----+---------+------------+------------+
#
#
import prettytable
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, Query


engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class City(db):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_ru = Column(String)
    population = Column(Integer)


db.metadata.create_all()

with Session() as session:
    pass  # TODO напишите Ваш запрос здесь


# Не удаляйте код ниже, он нужен, чтобы вывести результат запроса
cursor = engine.execute(Query(City).statement).cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
