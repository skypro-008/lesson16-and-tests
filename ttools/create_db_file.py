from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    full_name = db.Column(db.String)
    city = db.Column(db.Integer)
    city_ru = db.Column(db.String)


db.drop_all()
db.create_all()


data = [{'email': 'novlu@mail.com', 'password': 'mkdXjIjYM', 'full_name': 'Людмила Новикова', 'city': 10,
         'city_ru': 'Санкт-Петербург', 'id': 1},
        {'email': 'tripper678@yahhaa.com', 'password': 'eGGPtRKS5', 'full_name': 'Андрей Васечкин', 'city': 11,
         'city_ru': 'Москва', 'id': 2},
        {'email': 'georgiberidze@mail.com', 'password': 'NWRV0Z9ZC', 'full_name': 'Георги Беридзе', 'city': 7,
         'city_ru': 'Тбилиси', 'id': 3},
        {'email': 'oksi.laslas89@mail.com', 'password': 'TenhtQOjv', 'full_name': 'Оксана Ласкина', 'city': 12,
         'city_ru': 'Казань', 'id': 4},
        {'email': 'vanyahot888@inmail.com', 'password': '5YGRPtYlw', 'full_name': 'Иван Горячий', 'city': 13,
         'city_ru': 'Сочи', 'id': 5},
        {'email': 'yanaturkiy@mail.com', 'password': 'rN3HI4elT', 'full_name': 'Яна Ивлева', 'city': 4,
         'city_ru': 'Стамбул', 'id': 6},
        {'email': 'irafromrome@yahhaa.com', 'password': 'mWmSmkNsD', 'full_name': 'Ирина Самидзе', 'city': 1,
         'city_ru': 'Рим', 'id': 7},
        {'email': 'pskovstalker@mail.com', 'password': 'M572gH5lG', 'full_name': 'Владислав Ванькин', 'city': 14,
         'city_ru': 'Псков', 'id': 8},
        {'email': 'dinadina13@mail.com', 'password': 'v2dSbgPYb', 'full_name': 'Дина Левинова', 'city': 9,
         'city_ru': 'Хельсинки', 'id': 9},
        {'email': 'mark.loud@mail.com', 'password': 'pz4ZIYu1l', 'full_name': 'Марк Звонкий', 'city': 15,
         'city_ru': 'Нижний Новгород', 'id': 10}]


for user in data:
    instance = User(
        id=user.get('id'),
        email=user.get('email'),
        full_name=user.get('full_name'),
        password=user.get('password'),
        city=user.get('city'),
        city_ru=user.get('city_ru'))

    with db.session.begin():
        db.session.add(instance)


session = db.session()
cursor = session.execute("SELECT * from user").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)

# 
# 
# 
# 
# 
# 
# 
# 
# 