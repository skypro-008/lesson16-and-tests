import prettytable
from sqlalchemy import create_engine, Integer, Column, String, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Singer(db):
    __tablename__ = 'singer'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer, CheckConstraint("age < 35"))
    group = Column(String, nullable=False)


# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели

db.metadata.drop_all()
db.metadata.create_all()
session = Session()
cursor = session.execute("SELECT * from singer").cursor
mytable = prettytable.from_db_cursor(cursor)

if __name__ == '__main__':
    print(mytable)
