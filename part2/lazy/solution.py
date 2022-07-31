from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

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

    guide = relationship("Guide", back_populates="tours", lazy=True)


def get_tours_by_guide(guide_id):
    with Session() as session:
        guide = session.query(Guide).filter(Guide.id == guide_id).one()
        return guide.tours


def get_guide_by_tour(tour_id):
    with Session() as session:
        tour = session.query(Tour).filter(Tour.id == tour_id).one()
        return tour.guide
