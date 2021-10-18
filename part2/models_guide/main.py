# Допишите модели гид(Guide) экскурсия (Excursion)
# в соответствии с ulm (схема расположена в корне папки задания)
#
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    main_speciality = db.Column(db.String)
    country = db.Column(db.String)


class Excursion(db.Model):
    __tablename__ = 'excursion'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    guide_id = db.Column(db.Integer, db.ForeignKey('guide.id'))
    guide = db.relationship("Guide")

# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели


db.drop_all()
db.create_all()
session = db.session()
cursor = session.execute("SELECT * from author").cursor
mytable = prettytable.from_db_cursor(cursor)
cursor = session.execute("SELECT * from book").cursor
mytable2 = prettytable.from_db_cursor(cursor)

if __name__ == '__main__':
    print(mytable)
    print(mytable2)
