from sqlalchemy.orm import Session
from .models import models, schemas

# Movies

def get_movie(db: Session, id: str):
    # return db.query(models.Movie).filter_by(movie_id=id).first()
    return db.get(models.Movie, id)


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

def remove_movie(db: Session, id: int):
    db_movie = db.get(models.Movie, id)
    db.delete(db_movie)
    db.commit()
    # db.refresh(db_movie)
    return db_movie

# User

def get_user(db: Session, id: int):
    return db.get(models.User, id)


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter_by(username=username).first()

def get_users(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.User).offset(skip).limit(limit).all()

# def create_user_init(db: Session, user=schemas.UserCreate):
    # db_user = models.User(**user.dict())
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user

def create_user(db: Session, user=schemas.UserInDB):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Ratings

def get_ratings(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.Rating).offset(skip).limit(limit).all()

def get_rating(db: Session, movie_id: str, user_id: int):
    return db.get(models.Rating, (user_id,movie_id))
    
def get_ratings_by_user(db: Session, user_id: int):
    print(type(user_id), user_id)
    return db.query(models.Rating).filter(models.Rating.user_id==user_id).all()

def get_ratings_by_movie(db: Session, movie_id: str):
    return db.query(models.Rating).filter(models.Rating.movie_id==movie_id).all()


def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return rating

def update_rating(db: Session, rating:schemas.RatingCreate):
    db_rating = db.get(models.Rating, (rating.user_id,rating.movie_id))
    # db.merge(db_rating)
    # db_rating.rating = rating.rating
    setattr(db_rating, 'rating', rating.rating)
    db.commit()
    db.refresh(db_rating)
    return rating

def remove_rating(db: Session, rating:schemas.Rating):
    db_rating = db.get(models.Rating, (rating.user_id, rating.movie_id))
    db.delete(db_rating)
    db.commit()
    # db.refresh(db_movie)
    return rating


# Comments


def get_comments(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def get_comment(db: Session, id):
    return db.get(models.Comment, id)

def get_comments_by_user(db: Session, user_id: int):
    print(type(user_id), user_id)
    return db.query(models.Comment).filter(models.Comment.user_id==user_id).all()

def get_comments_by_movie(db: Session, movie_id: str):
    return db.query(models.Comment).filter_by(movie_id=movie_id).all()


def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment) 
    return db_comment

def update_comment(db: Session, comment:schemas.Comment):
    db_comment = db.get(models.Comment, comment.id)
    # db.merge(db_comment)
    # db_comment.comment = comment.comment
    setattr(db_comment, 'comment', comment.comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def remove_comment(db: Session, comment:schemas.Comment):
    db_comment = db.get(models.Comment, comment.id)
    db.delete(db_comment)
    db.commit()
    # db.refresh(db_movie)
    return db_comment


# MovieLists


def get_movie_lists(db: Session, skip: int = 0, limit: int = 250):
    return db.query(models.MovieList).offset(skip).limit(limit).all()

def get_movie_list(db: Session, id: int):
    return db.get(models.MovieList, id)

# def get_movie_lists_by_user(db: Session, user_id: int):
#     print(type(user_id), user_id)
#     return db.query(models.MovieList).filter(models.MovieList.user_id==user_id).all()

# def get_movie_lists_by_movie(db: Session, movie_title: str, movie_year:int):
#     return db.query(models.MovieList).filter(models.MovieList.movie_title==movie_title, models.MovieList.movie_year==movie_year).all()


def create_movie_list(db: Session, movie_list: schemas.MovieListCreate):
    db_movie_list = models.MovieList(**movie_list.dict())
    db.add(db_movie_list)
    db.commit()
    db.refresh(db_movie_list) 
    return db_movie_list

def update_movie_list(db: Session, movie_list:schemas.MovieList):
    db_movie_list = db.get(models.MovieList, movie_list.id)
    # db.merge(db_movie_list)
    # db_movie_list.movie_list = movie_list.movie_list
    setattr(db_movie_list, 'movie_list', movie_list.movies)
    db.commit()
    db.refresh(db_movie_list)
    return db_movie_list

def remove_movie_list(db: Session, id: int):
    db_movie_list = db.get(models.MovieList, id)
    db.delete(db_movie_list)
    db.commit()
    # db.refresh(db_movie)
    return db_movie_list