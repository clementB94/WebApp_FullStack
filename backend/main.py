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
from .api import crud, movies, users, ratings,comments, movie_lists, login


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="API WebApp")




# Routes 
app.include_router(users.router)
app.include_router(login.router)
app.include_router(movies.router)
app.include_router(ratings.router)
app.include_router(comments.router)
# app.include_router(movie_lists.router)
# CORS
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=["http://localhost:8080"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)


