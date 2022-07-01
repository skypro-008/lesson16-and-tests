import prettytable
from sqlalchemy import create_engine, Integer, Column, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Author(db):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True)
    first_name = Column(Text(200))
    last_name = Column(Text(200))


class Book(db):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True)
    title = Column(Text(200))
    copyright = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship("Author")

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
