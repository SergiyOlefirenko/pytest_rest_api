from sqlalchemy import Column, Integer, String, Float, DateTime
from src.DAL.db import Base


class Film(Base):

    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    replacement_cost = Column(Float)


class Language(Base):

    __tablename__ = 'language'

    language_id = Column(Integer, primary_key=True)
    name = Column(String)
    last_update = Column(DateTime)
