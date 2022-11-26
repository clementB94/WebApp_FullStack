from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import scraping
from .api.models import models, schemas
from .database import SessionLocal, engine, get_db
from .api import crud, movies, users, ratings,comments, movie_lists


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="API WebApp")

templates = Jinja2Templates(directory="frontend_old/")



# Routes 
app.include_router(users.router)
app.include_router(movies.router)
app.include_router(ratings.router)
app.include_router(comments.router)
app.include_router(movie_lists.router)
# CORS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=["http://localhost:8080"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporaire pour que le front marche
# @app.get("/")
# def get_movies(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     movies = crud.get_movies(db, skip=skip, limit=limit)

#     return templates.TemplateResponse('home.html', context={'request': request, 'imdb': movies})

# @app.get("/{title}")
# def get_movie_by_title(request: Request, title: str, db: Session = Depends(get_db)):
#     movie = crud.get_movie_by_title(db, title=title)
#     if movie is None:
#         raise HTTPException(status_code=404, detail=f"{title} not found")

    
#     movie = movie.__dict__
#     movie.pop('_sa_instance_state', None)
#     return templates.TemplateResponse('movie.html', context={'request': request, 'movie': movie})




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
