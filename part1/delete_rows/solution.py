import prettytable
from sqlalchemy import create_engine, text, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from guides_sql import CREATE_TABLE, INSERT_VALUES

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

with Session() as session:
    session.execute(text(CREATE_TABLE))
    session.execute(text(INSERT_VALUES))
    session.commit()


class Guide(db):
    __tablename__ = 'guide'
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    full_name = Column(String)
    tours_count = Column(Integer)
    bio = Column(String)
    is_pro = Column(Boolean)
    company = Column(Integer)


def delete_guides():
    with Session() as ses:
        ses.query(Guide).filter(Guide.id.in_((1, 4, 7))).delete()
        ses.commit()


delete_guides()
session = Session()
cursor = session.execute("SELECT * FROM guide").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print('БАЗА ДАННЫХ:')
    print(mytable)
