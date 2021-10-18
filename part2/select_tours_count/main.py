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
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean
import prettytable
import sqlite3
import os

workdir = os.getcwd()                   # для удобства выполнения заданий
source = sqlite3.connect('../db.main')  # связанных с работой в БД с помощью
dest = sqlite3.connect('./guides.db')   # этих функций каждый раз при заупске
source.backup(dest)                     # создаём учебный экземпляр базы данных
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guides.db'
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)


def do_request():
    result = db.session.query(Guide).filter(Guide.tours_count > 3).all()
    return result


session = db.session()
cursor = session.execute("SELECT * from guide").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == "__main__":
    print(mytable)
    os.remove('./guides.db')
