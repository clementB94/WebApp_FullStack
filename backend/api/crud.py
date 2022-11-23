from sqlalchemy.orm import Session
from .models import models, schemas

# Movies

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
# User
def get_users(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user_init(db: Session, user=schemas.UserCreate):
    db_rating = models.User(**user.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating
# Ratings
def get_ratings(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.Rating).offset(skip).limit(limit).all()



def get_rating(db: Session, movie_title: str, movie_year:int, user_id: int):
    return db.query(models.Rating).filter_by(movie_title=movie_title, movie_year=movie_year, user_id=user_id).first()

def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def update_rating(db: Session, rating:schemas.Rating):
    db_rating = db.get(models.Rating, (rating.user_id,rating.movie_title,rating.movie_year))
    # db.merge(db_rating)
    # db_rating.rating = rating.rating
    setattr(db_rating, 'rating', rating.rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating

def remove_rating(db: Session, rating:schemas.Rating):
    db_rating = db.get(models.Rating, (rating.user_id, rating.movie_title,rating.movie_year))
    db.delete(db_rating)
    db.commit()
    # db.refresh(db_movie)
    return 
