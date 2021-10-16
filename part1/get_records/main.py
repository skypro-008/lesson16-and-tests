# Имеется модель и заполненная база данных.
# 1. Напишите функцию get_all() которая будет возвращать все объекты из базы
# 2. Напишите функцию get_one() которая будет принимать аргумент id и
#  возвращать объект из базы, в соответствии с полученным аргументом.
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    full_name = db.Column(db.String)
    city = db.Column(db.Integer)
    city_ru = db.Column(db.String)


def get_all():
    pass
    # TODO напишите своё решение здесь


def get_one(id):
    pass
    # TODO напишите своё решение здесь
