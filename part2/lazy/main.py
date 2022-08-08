# В условии задачи даны две таблицы:
# guides:
# +----+--------+-------------+
# | id |  name  |   surname   |
# +----+--------+-------------+
# | 1  | Елена  |   Макеева   |
# | 2  | Федор  | Земельников |
# | 3  | Степан |  Саровский  |
# +----+--------+-------------+
#
# tours:
# +----+--------------------+---------------+----------+
# | id |        name        | days_duration | guide_id |
# +----+--------------------+---------------+----------+
# | 1  | Путешествие в горы |       4       |    1     |
# | 2  |    Лесные реки     |       2       |    1     |
# | 3  |  Сказки у костра   |       3       |    1     |
# | 4  |   Мир водопадов    |       7       |    2     |
# | 5  |    Зеленые луга    |       2       |    2     |
# | 6  |  Северная природа  |       4       |    2     |
# | 7  |    Ночной город    |       1       |    2     |
# | 8  |  Тайны Петербурга  |       1       |    3     |
# | 9  |    Три крепости    |       3       |    3     |
# | 10 |   Каньон желаний   |       7       |    3     |
# +----+--------------------+---------------+----------+
#
#
# После того как мы настроили relationship, нам предстоит
# 1. Написать функцию get_tours_by_guide(guide_id) - которая будет принимать id Гида
# и возвращать туры которые он проводит
#
# 2. Написать функцию get_guide_by_tour(tour_id) - которая будет принимать id Тура
# и возвращать гида, который проводит этот тур.

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from prettytable import prettytable
from guides_sql import add_tours, add_guides

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Guide(db):
    __tablename__ = 'guides'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    tours = relationship("Tour", back_populates="guide", lazy=True)


class Tour(db):

    __tablename__ = 'tours'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    days_duration = Column(Integer)
    guide_id = Column(ForeignKey("guides.id", ondelete="CASCADE"), nullable=False)

    guide = relationship("Guide", back_populates="tours", lazy=True)


def get_tours_by_guide(guide_id):
    # TODO напишите Ваш код здесь
    pass


def get_guide_by_tour(tour_id):
    # TODO напишите Ваш код здесь
    pass


# Ниже проверочный код Ваших функций,
# И тур по гиду с id = 3
if __name__ == "__main__":
    db.metadata.create_all()
    add_guides(Session, Guide)
    add_tours(Session, Tour)

    # возвращаем гида по туру с id = 2
    guide = get_guide_by_tour(2)
    print("Гид тура с ID=2:")
    columns = ['id', 'name', 'surname']
    mytable_guide = prettytable.PrettyTable()
    row = [guide.id, guide.name, guide.surname]
    mytable_guide.field_names = columns
    mytable_guide.add_row(row)
    print(mytable_guide)

    # Возвращаем туры гида с id = 2
    tours = get_tours_by_guide(2)
    print("Туры гида с ID=2:")
    columns = ['id', 'name', 'guide_id']
    mytable_one = prettytable.PrettyTable()
    rows = [[tour.id, tour.name, tour.guide_id] for tour in tours]
    mytable_one.field_names = columns
    mytable_one.add_rows(rows)
    print(mytable_one)
