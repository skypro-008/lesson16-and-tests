# Имеется наполненная БД с таблицей guide и полуготовый код на фласке.
# Напишите представления для следующих ендпоинтов:
#
# Method: GET
# URL: /guides
# Response: [{guide_json}, {guide_json}, {guide_json}]
#
# Method: GET
# URL: /guides/1
# Response: { <guide_json> }
#
#
from flask import Flask
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy
from guides_sql import CREATE_TABLE, INSERT_VALUES

import prettytable
from sqlalchemy import create_engine, text, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from guides_sql import CREATE_TABLE, INSERT_VALUES

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
with Session() as session:
    session.execute(text(CREATE_TABLE))
    session.execute(text(INSERT_VALUES))
    session.commit()


class Guide(db.Model):
    __tablename__ = 'guide'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)


@app.route("/guides")
def get_guides():
    # TODO допишите представления
    pass


@app.route("/guides/<int:gid>")
def get_guide(gid):
    # TODO допишите представления
    pass

# чтобы увидеть результат работы функций
# запустите фаил и
# перейдите по адресу:
# 127.0.0.1:5000/guides
# 127.0.0.1:5000/guides/1


if __name__ == "__main__":
    app.run()
