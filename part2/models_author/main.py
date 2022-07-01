# Напишите модели автор(Author) и книга (Book)
# в соответствии с uml (схема в файле tables.png в папке задания)
#
#
import prettytable
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Author(db):
    __tablename__ = "author"
    # TODO добавьте поля модели здесь


class Book(db):
    __tablename__ = "book"
    # TODO добавьте поля модели здесь

# Не удаляйте код ниже, он нужен для корректного
# отображения созданной вами модели


db.metadata.create_all()
session = Session()
cursor_author = session.execute("SELECT * from author").cursor
mytable = prettytable.from_db_cursor(cursor_author)
cursor_book = session.execute("SELECT * from book").cursor
mytable2 = prettytable.from_db_cursor(cursor_book)

if __name__ == '__main__':
    print(mytable)
    print(mytable2)
