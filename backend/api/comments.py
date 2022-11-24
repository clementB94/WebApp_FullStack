
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db, engine
from .. import scraping

router = APIRouter()

@router.get("/comments/", response_model=list[schemas.Comment], tags=["comments"])
def get_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_comments(db, skip=skip, limit=limit)
    return movies

@router.get("/comments/user", response_model=list[schemas.Comment], tags=["comments","users"])
def get_comment_by_user(user_id: int, db: Session = Depends(get_db)):
    movies = crud.get_comments_by_user(db, user_id)
    return movies

@router.get("/comments/movie", response_model=list[schemas.Comment], tags=["comments","movies"])
def get_comment_by_movie(movie_title: str, movie_year: int, db: Session = Depends(get_db)):
    movies = crud.get_comments_by_movie(db, movie_title, movie_year)
    return movies

@router.post("/comments/", response_model=schemas.Comment, tags=["comments"])
def add_comment(comment: schemas.Comment, db: Session = Depends(get_db)) :
    db_comment = crud.get_comment(db, comment.movie_title, comment.movie_year, comment.user_id)
    if db_comment:
        # raise HTTPException(status_code=400, detail=f"{movie.movie_title} already in base.")
        return crud.update_comment(db=db, comment=comment)
    return crud.create_comment(db=db, comment=comment)