import json

from flask import Flask, jsonify
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


@app.route("/guides")
def get_guides():
    guides = Guide.query.all()
    result = []
    for guide in guides:
        result.append({
            "id": guide.id,
            "surname": guide.surname,
            "full_name": guide.full_name,
            "tours_count": guide.tours_count,
            "bio": guide.bio,
            "is_pro": guide.is_pro,
            "company": guide.company,
        })
    return jsonify(result)


@app.route("/guides/<int:id>")
def get_user(id):
    guide = Guide.query.get(id)
    return {
        "id": guide.id,
        "surname": guide.surname,
        "full_name": guide.full_name,
        "tours_count": guide.tours_count,
        "bio": guide.bio,
        "is_pro": guide.is_pro,
        "company": guide.company,
    }


if __name__ == "__main__":
    pass
