from uuid import UUID
from sqlalchemy import Boolean, Column, ForeignKey, ForeignKeyConstraint, Integer, String, Float,Identity
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import relationship

from ...database import Base

class Movie(Base):
    __tablename__ = "movies"

    # movie_id = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(String, primary_key=True)
    title = Column(String)
    rating = Column(Float)
    year = Column(Integer) 
    # year = Column(Integer) 
    star_cast = Column(String)

class User(Base):
    __tablename__ = "users"

    # id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, primary_key=True)
    email = Column(String)
    full_name = Column(String)
    disabled = Column(Boolean)
    hashed_password = Column(String)
    

class Rating(Base):
    __tablename__ = "ratings"

    username = Column(String, ForeignKey("users.username"), primary_key=True)
    movie_id = Column(String, ForeignKey("movies.id"), primary_key=True)
    
    rating = Column(Float)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, ForeignKey("users.username"))
    movie_id = Column(String,ForeignKey("movies.id"))
    comment = Column(String)
    

# class MovieList(Base):
#     __tablename__ = "movielists"
#     id = Column(Integer, Identity(), primary_key=True)
#     name = Column(String)
#     author = Column(Integer, ForeignKey("users.username"))
#     movies = Column(String)
    # movies = Column(MutableList.as_mutable(pickleType), default=[])
    # movies = relationship('MovieListMap', uselist=True, backref='movies')
    
# class MovieListMap(Base):
#     __tablename__ = 'movielistmap'

#     list_id = Column(Integer, ForeignKey('movielists.id'), primary_key=True)
#     movie_title = Column(String, primary_key=True)
#     movie_year = Column(Integer, primary_key=True)
#     __table_args__ = (ForeignKeyConstraint(["movie_title", "movie_year"],
#                                            ["movies.movie_title", "movies.year"]),
#                       {})