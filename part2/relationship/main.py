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
# Вам предстоит настроить связи (relationship) для таблиц Guide и Tour:
# 1. Дополнить модель Guide аттрибутом tours - который будет представлять собой ссылку
# на туры конкретного гида (используйте relationship)
#
# 2. Дополнить модель Tour аттрибутом guide, с помощью которого можно получить
# объект гида обращаясь объекту класса Tour.
#

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from guides_sql import add_tours, add_guides

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Guide(db):
    __tablename__ = 'guides'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    tours = # TODO определите здесь атрибут relationship


class Tour(db):

    __tablename__ = 'tours'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    days_duration = Column(Integer)
    guide_id = Column(ForeignKey("guides.id", ondelete="CASCADE"), nullable=False)

    guide = # TODO определите здесь атрибут relationship


if __name__ == "__main__":
    db.metadata.create_all()
    add_guides(Session, Guide)
    add_tours(Session, Tour)

