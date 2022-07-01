import prettytable
from sqlalchemy import create_engine, Integer, Column, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Guide(db):
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    main_speciality = Column(String)
    country = Column(String)


class Excursion(db):
    __tablename__ = 'excursion'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    guide_id = Column(Integer, ForeignKey('guide.id'))
    guide = relationship("Guide")

# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели


db.metadata.create_all()
session = Session()
cursor_guide = session.execute("SELECT * from guide").cursor
mytable = prettytable.from_db_cursor(cursor_guide)
cursor_excursion = session.execute("SELECT * from excursion").cursor
mytable2 = prettytable.from_db_cursor(cursor_excursion)

if __name__ == '__main__':
    print(mytable)
    print(mytable2)
