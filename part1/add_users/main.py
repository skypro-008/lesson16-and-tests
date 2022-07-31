# Добавление пользователей
#
# Дана модель User и таблица user.
#
# Добавьте в базу данных сведения о пользователях
# в соответствии с таблицей:
#
# +----+------------------------+-----------+------------------+-----------------+
# | id |         email          |  password |    full_name     |     city_ru     |
# +----+------------------------+-----------+------------------+-----------------+
# | 1  |     novlu@mail.com     | mkdXjIjYM | Людмила Новикова | Санкт-Петербург |
# | 2  | tripper678@yahhaa.com  | eGGPtRKS5 | Андрей Васечкин  |      Москва     |
# | 3  | georgiberidze@mail.com | NWRV0Z9ZC |  Георги Беридзе  |     Тбилиси     |
# | 4  | oksi.laslas89@mail.com | TenhtQOjv |  Оксана Ласкина  |      Казань     |
# | 5  | vanyahot888@inmail.com | 5YGRPtYlw |   Иван Горячий   |       Сочи      |
# +----+------------------------+-----------+------------------+-----------------+
#
#
import prettytable
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker, Query


engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class User(db):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(Text(200))
    password = Column(Text(200))
    full_name = Column(Text(200))
    city_ru = Column(Text(200))


db.metadata.create_all()

with Session() as session:
    pass  # TODO напишите Ваш код здесь


# Не удаляйте код ниже, он нужен, чтобы вывести результат запроса
cursor = engine.execute(Query(User).statement).cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
