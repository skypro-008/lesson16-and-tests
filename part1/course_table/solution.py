from sqlalchemy import create_engine, Column, Integer, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker, Query


engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Course(db):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(Text(200))
    subject = Column(Text(200))
    price = Column(Integer)
    weeks = Column(Float)


db.metadata.create_all()
cursor = engine.execute(Query(Course).statement).cursor
