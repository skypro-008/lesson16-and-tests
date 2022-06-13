from sqlalchemy import create_engine, text, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from users_sql import CREATE_TABLE, INSERT_VALUES

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
with Session() as session:
    session.execute(text(CREATE_TABLE))
    session.execute(text(INSERT_VALUES))
    session.commit()


class User(db):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    full_name = Column(String)
    price_per_hour = Column(Float)
    city = Column(String)

    @classmethod
    def delete(cls, id):
        with Session() as session:
            user = session.query(cls).get(id)
            session.delete(user)
            session.commit()

    @classmethod
    def update(cls, id, **kwargs):
        with Session() as session:
            user = session.query(cls).get(id)
            for key, value in kwargs.items():
                setattr(user, key, value)
            session.commit()

