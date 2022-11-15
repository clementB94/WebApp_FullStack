import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import app.scraping

class Database:
    def __init__(self):
        self.conn = self.connect()
        self.conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        # On vérifie si elle est pas remplie
        cursor = self.conn.cursor()
        # Pour récuperer la liste des tables crées
        query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        cursor.execute(query)
        table_list = cursor.fetchall()
        # IMDB
        print(table_list)
        if not table_list :
            self.init_IMDB()
        elif "imdb" not in table_list[:][0]:
            self.init_IMDB()
        # return response
        cursor.close()


        # self.cursor = self.conn.cursor() # A changer (potentiellement fuite de memoire)    

    def connect(self):
        print("Connecting to PostgreSQL Database...")
        try:
            conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="database", port="5432")
        except:
            print(f"Error, can't connect")
            # sys.exit(1)

        return conn
    
    def add_df_values(self, df, table):
        tuples = [tuple(x) for x in df.to_numpy()]

        cols = ','.join(list(df.columns))
        query = "INSERT INTO %s(%s) VALUES %%s" % (table, cols)
        cursor = self.conn.cursor()
        try:
            psycopg2.extras.execute_values(cursor, query, tuples)
            self.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error: %s" % error)
            self.conn.rollback()
            cursor.close()
            return 1
        print("the dataframe is inserted")
        cursor.close()

    def init_IMDB(self):
        query = """
        CREATE TABLE imdb (
                rank INTEGER,
                movie_title VARCHAR(255),
                rating FLOAT,
                year INTEGER,
                star_cast VARCHAR(255),
                PRIMARY KEY (movie_title , year)
        )
        """
        cursor = self.conn.cursor()
        cursor.execute(query)
        movies = app.scraping.scrap_movies_db()
        self.add_df_values(movies,"imdb")
        cursor.close()
        

    def get_movies(self):
        postgreSQL_select_Query = "select * from IMDB"
        cursor = self.conn.cursor()
        cursor.execute(postgreSQL_select_Query)
        imdb = cursor.fetchall()
        print(imdb)
        cursor.close()
        return imdb
    
    def test(self):
        query = f"SELECT datname  FROM pg_database;"
        cursor = self.conn.cursor()
        cursor.execute(query)
        response = cursor.fetchall()
        a = "postgre" in response[:][0]
        response = f"{response} \n {a}"
        cursor.close()
        return response
        # return {"a":"b"}
