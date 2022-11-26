from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

def scrap_movie_imdb(url:str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        id = [u for u in url.split("/") if u.startswith("tt")][0]
        title  = soup.find("h1", {"data-testid":"hero-title-block__title"}).getText()
        rating = soup.find("div", {"data-testid":"hero-rating-bar__aggregate-rating__score"}).span.getText()
        year = soup.find("ul", {"data-testid":"hero-title-block__metadata"})
        year = year.find("li", {"class":"ipc-inline-list__item"}).a.getText()
        # star_cast = soup.find_all(lambda tag: tag.name == "a" and "Casting principal" in tag.text)
        star_cast = soup.find_all("li",{"data-testid":"title-pc-principal-credit"})[-1]
        star_cast = ", ".join([star.getText() for star in star_cast.find_all("li")])

        movie = {
                "id": id,
                "title":title,
                "rating":rating,
                "year":year,
                "star_cast":star_cast
        }
        print(movie)
        return movie
                


def scrap_top_movies_imdb(limit=250) : 
        url = 'http://www.imdb.com/chart/top'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        # movies = soup.find_all("td.titleColumn a")
        scraped_movies = []
        # movies = soup.select('td.titleColumn')
        for a in soup.select('td.titleColumn a'):
                if limit:
                        limit-=1
                        movie_url = "https://www.imdb.com"+a.attrs.get('href')
                        try:
                                scraped_movies.append(scrap_movie_imdb(movie_url))
                        except:
                                print("Scraping error :",movie_url)
        return scraped_movies
    