import prettytable
from sqlalchemy import create_engine, text, Column, Integer, String
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
    city = Column(Integer)
    city_ru = Column(String)

    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.query(cls).all()

    @classmethod
    def get_one(cls, user_id):
        with Session() as session:
            return session.query(cls).filter(cls.id == user_id).one()


# не удаляйте код ниже, он используется для вывода на экран
# результата выполнения составленных вами функций
if __name__ == "__main__":
    mytable_one = prettytable.PrettyTable()
    mytable_all = prettytable.PrettyTable()
    columns = [
        'id', 'email', 'password',
        'full_name', 'city', 'city_ru']
    mytable_one.field_names = columns
    mytable_all.field_names = columns
    rows = [[x.id, x.email, x.password,
             x.full_name, x.city, x.city_ru] for x in User.get_all()]
    obj = User.get_one(1)
    row = [obj.id, obj.email, obj.password,
           obj.full_name, obj.city,
           obj.city_ru]

    mytable_all.add_rows(rows)
    mytable_one.add_row(row)
    print('get_one:')
    print(mytable_one)
    print('get_all:')
    print(mytable_all)
