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
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Ratings

def get_ratings(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.Rating).offset(skip).limit(limit).all()

def get_rating(db: Session, movie_title: str, movie_year:int, user_id: int):
    return db.query(models.Rating).filter_by(movie_title=movie_title, movie_year=movie_year, user_id=user_id).first()

def get_ratings_by_user(db: Session, user_id: int):
    print(type(user_id), user_id)
    return db.query(models.Rating).filter(models.Rating.user_id==user_id).all()

def get_ratings_by_movie(db: Session, movie_title: str, movie_year:int):
    return db.query(models.Rating).filter(models.Rating.movie_title==movie_title, models.Rating.movie_year==movie_year).all()


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
    return db_rating


# Comments


def get_comments(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def get_comment(db: Session, movie_title: str, movie_year:int, user_id: int):
    return db.query(models.Comment).filter_by(movie_title=movie_title, movie_year=movie_year, user_id=user_id).first()

def get_comments_by_user(db: Session, user_id: int):
    print(type(user_id), user_id)
    return db.query(models.Comment).filter(models.Comment.user_id==user_id).all()

def get_comments_by_movie(db: Session, movie_title: str, movie_year:int):
    return db.query(models.Comment).filter(models.Comment.movie_title==movie_title, models.Comment.movie_year==movie_year).all()


def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment) 
    return db_comment

def update_comment(db: Session, comment:schemas.Comment):
    db_comment = db.get(models.Comment, (comment.user_id,comment.movie_title,comment.movie_year))
    # db.merge(db_comment)
    # db_comment.comment = comment.comment
    setattr(db_comment, 'comment', comment.comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def remove_comment(db: Session, comment:schemas.Comment):
    db_comment = db.get(models.Comment, (comment.user_id, comment.movie_title,comment.movie_year))
    db.delete(db_comment)
    db.commit()
    # db.refresh(db_movie)
    return db_comment