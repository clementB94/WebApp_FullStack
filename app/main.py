from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import psycopg2
import numpy as np
import psycopg2.extras as extras
#from insert_db import insert_db
from app.database import Database

app = FastAPI(title="API WebApp")
db = Database()



    

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



@app.get('/')
def Home():

    # conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="database", port="5432")
    # cursor = conn.cursor()
    # postgreSQL_select_Query = "select * from IMDB"
    # cursor.execute(postgreSQL_select_Query)
    # imdb = cursor.fetchall()
    imdb = db.get_movies()
    
    return {row for row in imdb}

@app.get('/test')
def test():

    return db.test()


# insert_db()