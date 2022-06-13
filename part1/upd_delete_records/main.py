# Имеется модель и заполненная база данных.
# 1. Напишите метод delete() модели User, который будет принимать аргумент id и
#  удалять объект из базы, в соответствии с полученным аргументом.
# 2. Напишите метод update() модели User, который будет принимать аргумент id и
#  обновлять объект в базе, в соответствии с полученными аргументами.


import prettytable
from sqlalchemy import create_engine, text, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from users_sql import CREATE_TABLE, INSERT_VALUES

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
with Session() as session:
    session.execute(text(CREATE_TABLE))
    session.execute(text(INSERT_VALUES))
    session.commit()


class User(db):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    price_per_hour = Column(Float)
    city = Column(String)

    @classmethod
    def delete(cls, id):
        pass  # TODO напишите метод для модели здесь

    @classmethod
    def update(cls, id, **kwargs):
        pass  # TODO напишите метод для модели здесь

