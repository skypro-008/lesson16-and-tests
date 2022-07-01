# Городская таблица
# Определите поля для модели City по таблице city:
# +----+---------+------------+------------+
# | id |   name  | country_ru | population |
# +----+---------+------------+------------+
# | 1  |   Рим   |   Италия   |  2873000   |
# | 2  |  Милан  |   Италия   |  1333000   |
# | 3  | Венеция |   Италия   |   265000   |
# +----+---------+------------+------------+
#
#
import prettytable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Query


engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class City(db):
    __tablename__ = 'city'
    pass  # TODO добавьте в модель необходимые колонки


# Не удаляйте код ниже, он нужен для корректного отображения
# созданной вами модели при запуске файла

db.metadata.create_all()
cursor = engine.execute(Query(City).statement).cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30


if __name__ == '__main__':
    print(mytable)
