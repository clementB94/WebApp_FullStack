
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db, engine
from .. import scraping

router = APIRouter()



# ======== GET ========

@router.get("/movies/{title}", response_model=schemas.Movie, tags=["movies"])
def get_movie_by_title(title: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=title)
    if db_movie is None:
        raise HTTPException(status_code=404, detail=f"{title} not found")
    return db_movie

@router.get("/movies/", response_model=list[schemas.Movie])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies

# ======== POST ========

@router.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=movie.movie_title)
    if db_movie:
        raise HTTPException(status_code=400, detail=f"{movie.movie_title} already in base.")
    return crud.create_movie(db=db, movie=movie)

@router.post("/movies/250_most_rated")
def scrape_movies():
    scraped_movies = scraping.scrap_movies_db()
    return scraped_movies.to_sql(
        'movies', 
        con=engine, 
        if_exists='append', 
        index=False)


# ======== DELETE ========

@router.delete("/movies/{title}", response_model=schemas.Movie)
def delete_movie(title: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=title)
    if not db_movie:
        raise HTTPException(status_code=400, detail=f"{title} don't find in base.")
    return crud.remove_movie(db=db, title=db_movie.movie_title, year=db_movie.year)

