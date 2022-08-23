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
    def get_freelancers(cls):
        with Session() as ses:
            freelancers = ses.query(cls).filter_by(company=None).all()
        return freelancers


# не удаляйте код ниже, он необходим
# для выдачи результата запроса


mytable = prettytable.PrettyTable()
mytable.field_names = [
    'id', 'surname', 'full_name',
    'tours_count', 'bio', 'is_pro', 'company']

rows = [[x.id, x.surname, x.full_name,
         x.tours_count, x.bio, x.is_pro, x.company] for x in Guide.get_freelancers()]
mytable.add_rows(rows)
mytable.max_width = 25

if __name__ == "__main__":
    print('Запрос возвращает следующие записи:')
    print(mytable)