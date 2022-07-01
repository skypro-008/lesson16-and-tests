# Допишите модели гид(Guide) экскурсия (Excursion)
# в соответствии с ulm (схема расположена в корне папки задания)
#
import prettytable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Guide(db):
    __tablename__ = 'guide'
    # TODO напишите поля модели здесь


class Excursion(db):
    __tablename__ = 'excursion'
    # TODO напишите поля модели здесь

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
