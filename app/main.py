from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, scraping
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API WebApp")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


templates = Jinja2Templates(directory="frontend/")

# ======== GET ========

# @app.get("/movies/{id}", response_model=schemas.Movie)
# def get_movie(id: int, db: Session = Depends(get_db)):
#     db_movie = crud.get_movie(db, id=id)
#     if db_movie is None:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return db_movie

@app.get("/movies/{title}", response_model=schemas.Movie)
def get_movie_by_title(title: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=title)
    if db_movie is None:
        raise HTTPException(status_code=404, detail=f"{title} not found")
    return db_movie

@app.get("/movies/", response_model=list[schemas.Movie])
def get_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)
    return movies

# Temporaire pour que le front marche
@app.get("/")
def get_movies(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = crud.get_movies(db, skip=skip, limit=limit)

    return templates.TemplateResponse('home.html', context={'request': request, 'imdb': movies})

@app.get("/{title}")
def get_movie_by_title(request: Request, title: str, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_title(db, title=title)
    if movie is None:
        raise HTTPException(status_code=404, detail=f"{title} not found")

    
    movie = movie.__dict__
    movie.pop('_sa_instance_state', None)
    return templates.TemplateResponse('movie.html', context={'request': request, 'movie': movie})


# ======== POST ========

@app.post("/movies/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=movie.movie_title)
    if db_movie:
        raise HTTPException(status_code=400, detail=f"{movie.movie_title} already in base.")
    return crud.create_movie(db=db, movie=movie)

@app.post("/movies/250_most_rated")
def scrape_movies():
    scraped_movies = scraping.scrap_movies_db()
    return scraped_movies.to_sql(
        'movies', 
        con=engine, 
        if_exists='append', 
        index=False)


# ======== DELETE ========

# @app.delete("/movies/{id}", response_model=schemas.Movie)
# def delete_movie(id: int, db: Session = Depends(get_db)):
#     db_movie = crud.get_movie(db, id=id)
#     if not db_movie:
#         raise HTTPException(status_code=400, detail=f"ID {id} don't find in base.")
#     return crud.remove_movie(db=db, id=id)

@app.delete("/movies/{title}", response_model=schemas.Movie)
def delete_movie(title: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=title)
    if not db_movie:
        raise HTTPException(status_code=400, detail=f"{title} don't find in base.")
    return crud.remove_movie(db=db, title=db_movie.movie_title, year=db_movie.year)





# @app.get('/')
# def Home(request: Request):

#     imdb = db.get_movies()

#     return templates.TemplateResponse('home.html', context={'request': request, 'imdb': imdb})

# @app.get('/{title}')
# def movie(request: Request, title: str):

#     imdb = db.get_movies()
#     movie = [movie for movie in imdb if movie[1] == title]

#     return templates.TemplateResponse('movie.html', context={'request': request, 'movie': movie})

# @app.get('/test')
# def test():

#     return db.test()
