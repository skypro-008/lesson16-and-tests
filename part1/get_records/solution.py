from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.users'
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
    all_users = User.query.all()
    return all_users


def get_one(id):
    one_user = User.query.get(id)
    return one_user
