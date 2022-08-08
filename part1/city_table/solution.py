from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Query


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
cursor = engine.execute(Query(City).statement).cursor
