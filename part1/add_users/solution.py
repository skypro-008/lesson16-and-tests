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
Ludmila = User(
    id=1,
    email="novlu@mail.com",
    password="mkdXjIjYM",
    full_name="Людмила Новикова",
    city_ru="Санкт-Петербург")
Andrew = User(
    id=2,
    email="tripper678@yahhaa.com",
    password="eGGPtRKS5",
    full_name="Андрей Васечкин",
    city_ru="Москва")
George = User(
    id=3,
    email="georgiberidze@mail.com",
    password="NWRV0Z9ZC",
    full_name="Георги Беридзе",
    city_ru="Тбилиси")
Oksana = User(
    id=4,
    email="oksi.laslas89@mail.com",
    password="TenhtQOjv",
    full_name="Оксана Ласкина",
    city_ru="Казань")
Ivan = User(
    id=5,
    password="5YGRPtYlw",
    full_name="Иван Горячий",
    email='vanyahot888@inmail.com',
    city_ru="Сочи")

users = (Ludmila, Andrew, George, Oksana, Ivan)

with Session() as session:
    session.add_all(users)
    session.commit()
