from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base

class Movie(Base):
    __tablename__ = "movies"

    # movie_id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer)
    movie_title = Column(String, primary_key=True)
    rating = Column(Float)
    year = Column(Integer, primary_key=True)
    star_cast = Column(String)