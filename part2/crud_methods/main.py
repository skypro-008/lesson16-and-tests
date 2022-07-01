# УРОК 16 Задание 8
# В этом финальном задании вам нужно
# применить знания о моделях для создания 5 методов,
# которые реализуют CRUD действия.

"""
    # Задание
    #
    # Шаг 1.
    # ######
    # Напишите метод модели Guide.get_all()
    # который возвращает список всех объектов из базы
    #
    # Шаг 2.
    # ######
    # Напишите метод модели Guide.get(guide_id)
    # который возвращает объект из базы
    # в соответствии с его id
    #
    # Шаг 3.
    # ######
    # Напишите метод модели Guide.delete(guide_id)
    # который удаляет объект из базы
    #
    # Шаг 4.
    # ######
    # Напишите метод модели Guide.create(**kwargs)
    # который добавляет объект в базу данных
    #
    # Шаг 5.
    # ######
    # Напишите метод модели Guide.filter_by_tours_count(tour_count)
    # который будет возвращать список объектов из базы данных в соответствии
    # с полученным количеством туров.
    #
"""

from sqlalchemy import create_engine, text, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from guides_sql import CREATE_TABLE, INSERT_VALUES

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

with Session() as session:
    session.execute(text(CREATE_TABLE))
    session.execute(text(INSERT_VALUES))
    session.commit()


class Guide(db):
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)

    @classmethod
    def get_all(cls):
        # TODO напишите Ваш код здесь
        pass

    @classmethod
    def get(cls, guide_id):
        # TODO напишите Ваш код здесь
        pass

    @classmethod
    def delete(cls, guide_id):
        # TODO напишите Ваш код здесь
        pass

    @classmethod
    def create(cls, **kwargs):
        # TODO напишите Ваш код здесь
        pass

    @classmethod
    def filter_by_tours_count(cls, tours_count):
        # TODO напишите Ваш код здесь
        pass
