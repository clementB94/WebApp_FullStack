from sqlalchemy.orm import Session
from . import models, schemas

def get_movie(db: Session, id: int):
    return db.query(models.Movie).filter_by(movie_id=id).first()


def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movie).filter_by(movie_title=title).first()

def get_movies(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie=schemas.MovieCreate):
    db_movie = models.Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def remove_movie(db: Session, title: str, year: int):
    db_movie = db.get(models.Movie, (title,year))
    db.delete(db_movie)
    db.commit()
    # db.refresh(db_movie)
    return db_movie