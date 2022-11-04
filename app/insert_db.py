from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import psycopg2
import numpy as np
import psycopg2.extras as extras


def execute_values(conn, df, table):
    
    tuples = [tuple(x) for x in df.to_numpy()]

    cols = ','.join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor, query, tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()


def insert_db() : 

    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.select('td.titleColumn')
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
            for b in soup.select('td.posterColumn span[name=ir]')]
    
    list = []
    
    for index in range(0, len(movies)):
        
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index))+1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index))-(len(movie))]
        data = {"place": place,
                "movie_title": movie_title,
                "rating": ratings[index],
                "year": year,
                "star_cast": crew[index],
                }
        list.append(data)
    
    df = pd.DataFrame(list)

    conn = psycopg2.connect(database="db", user='postgres', host='postgres:5432', port='27017')
    
    execute_values(conn, df, 'IMDB')