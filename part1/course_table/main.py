# Таблица сообщений
# Создайте модель Course по таблице courses:
# +----+-------------------+---------+-------+-------+
# | id |       title       | subject | price | weeks |
# +----+-------------------+---------+-------+-------+
# | 1  | Введение в Python |  Python | 11000 |  3.5  |
# | 2  |  Пишем на Spring  |   Java  | 15000 |  8.0  |
# | 3  |   Игры на Python  |  Python | 13500 |  5.0  |
# | 4  |    Игры на Java   |   Java  |  9000 |  4.5  |
# +----+-------------------+---------+-------+-------+
#
#
import prettytable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Query


engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


# TODO опишите модель Course здесь


# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла
db.metadata.create_all()
cursor = engine.execute(Query(Course).statement).cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
