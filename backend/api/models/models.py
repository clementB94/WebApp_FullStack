from sqlalchemy import Boolean, Column, ForeignKey, ForeignKeyConstraint, Integer, String, Float
from sqlalchemy.orm import relationship

from ...database import Base

class Movie(Base):
    __tablename__ = "movies"

    # movie_id = Column(Integer, primary_key=True, autoincrement=True)
    rank = Column(Integer)
    movie_title = Column(String, primary_key=True)
    rating = Column(Float)
    year = Column(Integer, primary_key=True) # TODO: combiner nom et year primary key (ForeignKeyConstraint)
    # year = Column(Integer) 
    star_cast = Column(String)

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    user_password = Column(String)

class Note(Base):
    __tablename__ = "notes"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    movie_title = Column(String, primary_key=True)
    movie_year = Column(Integer, primary_key=True)
    
    note = Column(Integer)
    __table_args__ = (ForeignKeyConstraint(["movie_title", "movie_year"],
                                           ["movies.movie_title", "movies.year"]),
                      {})

class Comment(Base):
    __tablename__ = "comments"

    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True, unique=True)
    movie_title = Column(String, primary_key=True)
    movie_year = Column(Integer, primary_key=True)
    comment = Column(String)
    
    __table_args__ = (ForeignKeyConstraint(["movie_title", "movie_year"],
                                           ["movies.movie_title", "movies.year"]),
                      {})