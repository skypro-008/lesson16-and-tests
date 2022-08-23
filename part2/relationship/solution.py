from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from guides_sql import add_tours, add_guides

engine = create_engine('sqlite:///:memory:')
db = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Guide(db):
    __tablename__ = 'guides'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    tours = relationship("Tour", back_populates="guide", lazy=True)


class Tour(db):

    __tablename__ = 'tours'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    days_duration = Column(Integer)
    guide_id = Column(ForeignKey("guides.id", ondelete="CASCADE"), nullable=False)

    guide = relationship("Guide", back_populates="tours")


if __name__ == "__main__":
    db.metadata.create_all()
    add_guides(Session, Guide)
    add_tours(Session, Tour)

