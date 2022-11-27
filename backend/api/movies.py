
from typing import Union
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db, engine
from .. import scraping

router = APIRouter()



# ======== GET ========

@router.get("/movies/", response_model=list[schemas.Movie], tags=["movies"])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies

@router.get("/movies/{id}", response_model=schemas.Movie, tags=["movies"])
def get_movie(id: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail=f"{id} not found")
    return db_movie

@router.get("/movies/title/", response_model=schemas.Movie, tags=["movies"])
def get_movie_by_title(title: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=title)
    if db_movie is None:
        raise HTTPException(status_code=404, detail=f"{title} not found")
    return db_movie



# ======== POST ========

@router.post("/movies/", response_model=schemas.Movie, tags=["movies"])
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie.id)
    if db_movie:
        raise HTTPException(status_code=400, detail=f"{movie.id} already in base.")
    return crud.create_movie(db=db, movie=movie)

@router.post("/movies/most_rated",response_model=list[schemas.Movie], tags=["movies"])
def scrape_top_movies(limit: int, db: Session = Depends(get_db)):
    scraped_movies = scraping.scrap_top_movies_imdb(limit)
    movies = []
    for movie in scraped_movies:
        try :
            movie = create_movie(schemas.MovieCreate(**movie), db)
            movies.append(movie)
        except:
            continue # Movie already in base
    return movies

@router.post("/movies/scrape/", tags=["movies"])
def scrape_movie(url: str, db: Session = Depends(get_db)):
    scraped_movie = scraping.scrap_movie_imdb(url)
    scraped_movie = schemas.MovieCreate(**scraped_movie)
    return crud.create_movie(db,scraped_movie)


# ======== DELETE ========

@router.delete("/movies/{id}", response_model=schemas.Movie, tags=["movies"])
def delete_movie(id: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, id)
    if not db_movie:
        raise HTTPException(status_code=400, detail=f"{id} don't find in base.")
    return crud.remove_movie(db, id)

