from pydantic import BaseModel

class MovieBase(BaseModel):
    rank:int
    movie_title:str
    rating:float
    year: int
    star_cast:str #TODO : str -> liste d'acteurs

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    class Config:
        orm_mode = True
    