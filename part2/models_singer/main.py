# Напишите модель певец (Singer) с именем таблицы "singer"
# Для данной модели заданы следующие ограничения:
#
#
# #Таблица singer, описание колонок:
# Идентификатор - первичный ключ (PK) - id
# Имя - должно быть уникальным - name
# Возраст - не больше 35 лет - age
# Группа - не может быть Null (None) - group
#
import prettytable
from sqlalchemy import create_engine, Integer, Column, String, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Singer(db):
    __tablename__ = 'singer'
    # TODO напишите поля модели здесь


# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели

db.metadata.drop_all()
db.metadata.create_all()
session = Session()
cursor = session.execute("SELECT * from singer").cursor
mytable = prettytable.from_db_cursor(cursor)
session.close()

if __name__ == '__main__':
    print(mytable)
