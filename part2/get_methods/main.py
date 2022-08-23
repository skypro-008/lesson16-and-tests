# Имеется наполненная БД с таблицей guide.
# Напишите 2 метода для таблицы Guide
#
# get_all() - возвращающий всех гидов
#
# get(guide_id) - возвращающий гида по id
#
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

    @classmethod
    def get_all(cls):
        # TODO напишите Ваш код здесь
        pass

    @classmethod
    def get(cls, guide_id):
        # TODO напишите Ваш код здесь
        pass
