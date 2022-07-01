from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class City(db):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_ru = Column(String)
    population = Column(Integer)


db.metadata.create_all()

Rome = City(
    id=1,
    name="Рим",
    country_ru="Италия",
    population=28730000)

Milan = City(
    id=2,
    name="Милан",
    country_ru="Италия",
    population=1333000)

Venice = City(
    id=3,
    name="Венеция",
    country_ru="Италия",
    population=265000)

Istanbul = City(
    id=4,
    name="Стамбул",
    country_ru="Турция",
    population=108950000)

Kemer = City(
    id=5,
    name="Кемер",
    country_ru="Турция",
    population=22421)

cities = (Rome, Milan, Venice, Istanbul, Kemer)

with Session() as session:
    session.add_all(cities)
    session.commit()
