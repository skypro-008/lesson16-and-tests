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
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.guides'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Guide(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String)
    full_name = db.Column(db.String)
    tours_count = db.Column(db.Integer)
    bio = db.Column(db.String)
    is_pro = db.Column(db.Boolean)
    company = db.Column(db.Integer)

# TODO исправьте представления:
# # # # # # # # #


@app.route("/guides")
def get_guides():
    guides = Guide.query.filter(Guide.company > 2).all()
    r = []
    for g in guides:
        if len(r) == 3:
            break
        r.append({
            "surname": g.surname,
        })

    return r


@app.route("/guides/", )
def get_user(gid: int):
    g = Guide.query.get(gid)
    return {
        "surname": g.surname,
    }
# # # # # # # # # # # # # # # # # # # # #
