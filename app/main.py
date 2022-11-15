from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import psycopg2
import numpy as np
import psycopg2.extras as extras
from app.database import Database

app = FastAPI(title="API WebApp")
templates = Jinja2Templates(directory="frontend/")

db = Database()


@app.get('/')
def Home(request: Request):

    imdb = db.get_movies()

    return templates.TemplateResponse('home.html', context={'request': request, 'imdb': imdb})

@app.get('/{title}')
def movie(request: Request, title: str):

    imdb = db.get_movies()
    movie = [movie for movie in imdb if movie[1] == title]

    return templates.TemplateResponse('movie.html', context={'request': request, 'movie': movie})

@app.get('/test')
def test():

    return db.test()
