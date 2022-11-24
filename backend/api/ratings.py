
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db, engine
from .. import scraping

router = APIRouter()

@router.get("/ratings/", response_model=list[schemas.Rating])
def get_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_ratings(db, skip=skip, limit=limit)
    return movies

@router.get("/ratings/user", response_model=list[schemas.Rating])
def get_rating_by_user(user_id: int, db: Session = Depends(get_db)):
    movies = crud.get_ratings_by_user(db, user_id)
    return movies

@router.get("/ratings/movie", response_model=list[schemas.Rating])
def get_rating_by_movie(movie_title: str, movie_year: int, db: Session = Depends(get_db)):
    movies = crud.get_ratings_by_movie(db, movie_title, movie_year)
    return movies

@router.post("/ratings/", response_model=schemas.Rating)
def add_rating(rating: schemas.Rating, db: Session = Depends(get_db)) :
    db_rating = crud.get_rating(db, rating.movie_title, rating.movie_year, rating.user_id)
    if db_rating:
        # raise HTTPException(status_code=400, detail=f"{movie.movie_title} already in base.")
        return crud.update_rating(db=db, rating=rating)
    return crud.create_rating(db=db, rating=rating)