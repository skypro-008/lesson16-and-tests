from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import prettytable

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db: SQLAlchemy = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text(200))


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text(200))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship("Author")

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
