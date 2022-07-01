# Напишите метод update_tours_count, который
# принимает аргумент guide_id и
# увеличивает значение поля tours_count на 1
#
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

    @classmethod
    def update_tours_counter(cls, guide_id):
        # TODO напишите Ваш код здесь
        pass

# не удаляйте код ниже, он необходим
# для выдачи результата запроса


Guide.update_tours_counter(1)
ses = Session()
cursor = ses.execute("SELECT * FROM guide WHERE `id`=1").cursor
mytable = prettytable.from_db_cursor(cursor)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
