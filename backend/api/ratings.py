
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db

router = APIRouter()

@router.get("/ratings/", response_model=list[schemas.Rating], tags=["ratings"])
def get_ratings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ratings = crud.get_ratings(db, skip=skip, limit=limit)
    return ratings

@router.get("/ratings/user", response_model=list[schemas.Rating], tags=["ratings","users"])
def get_rating_by_user(user_id: int, db: Session = Depends(get_db)):
    ratings = crud.get_ratings_by_user(db, user_id)
    return ratings

@router.get("/ratings/movie", response_model=list[schemas.Rating],tags=["ratings","movies"])
def get_rating_by_movie(movie_id: str, db: Session = Depends(get_db)):
    ratings = crud.get_ratings_by_movie(db, movie_id)
    return ratings

@router.post("/ratings/", response_model=schemas.RatingCreate, tags=["ratings"])
def add_rating(rating: schemas.RatingCreate, db: Session = Depends(get_db)) :
    db_rating = crud.get_rating(db, rating.movie_id, rating.user_id)
    if db_rating:
        return crud.update_rating(db=db, rating=rating)
    return crud.create_rating(db=db, rating=rating)

# ======== DELETE ========

@router.delete("/ratings/", response_model=schemas.Rating, tags=["ratings"])
def delete_rating(rating: schemas.Rating, db: Session = Depends(get_db)):
    db_rating = crud.get_rating(db, rating.movie_id, rating.user_id)
    if not db_rating:
        raise HTTPException(status_code=400, detail=f"Rating not found in base.")
    return crud.remove_rating(db=db, rating=rating)
