# Условия данной задачи содеражся в файле
# task.md в корне папки с заданием
#
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from guides_sql import CREATE_TABLE, INSERT_VALUES
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False
db = SQLAlchemy(app)
with db.session.begin():
    db.session.execute(text(CREATE_TABLE))
    db.session.execute(text(INSERT_VALUES))


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
def find_by_tc():
    tours_count = request.args.get("tours_count")
    guides = Guide.query.all()
    r = []
    if tours_count:
        for g in guides:
            if g.tours_count == int(tours_count):
                r.append({
                    "id": g.id,
                    "surname": g.surname,
                    "full_name": g.full_name,
                    "tours_count": g.tours_count,
                    "bio": g.bio,
                    "is_pro": g.is_pro,
                    "company": g.company,
                })
    else:
        for g in guides:
            r.append({
                "id": g.id,
                "surname": g.surname,
                "full_name": g.full_name,
                "tours_count": g.tours_count,
                "bio": g.bio,
                "is_pro": g.is_pro,
                "company": g.company,
            })
    return jsonify(r), 200


# 2, 4, 5
@app.route("/guides/<int:gid>", methods=['GET', 'POST', 'PUT'])
def find_by_id(gid: int):
    if request.method == "GET":
        g = Guide.query.get(gid)
        return json.dumps({
            "id": g.id,
            "surname": g.surname,
            "full_name": g.full_name,
            "tours_count": g.tours_count,
            "bio": g.bio,
            "is_pro": g.is_pro,
            "company": g.company,
        })
    elif request.method == "POST":
        Guide.query.filter(Guide.id == gid).delete(False)
        db.session.commit()
        return jsonify(""), 204
    elif request.method == "PUT":
        g = Guide.query.get(gid)
        data = json.loads(request.data)
        if "surname" in data:
            g.surname = data.get("surname")
        if "full_name" in data:
            g.full_name = data.get("full_name")
        if "tours_count" in data:
            g.tours_count = data.get("tours_count")
        db.session.commit()
        return jsonify(""), 204


if __name__ == "__main__":
    app.run()
