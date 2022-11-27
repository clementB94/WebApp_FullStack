from typing import Union
from pydantic import BaseModel

class MovieBase(BaseModel):
    id:str
    title:str
    rating:float
    year: int
    star_cast:str #TODO : str -> liste d'acteurs

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    class Config:
        orm_mode = True

# User

class UserBase (BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id:int
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str

#token

class Token(BaseModel):
    access_token: str
    token_type: str

        
# Rating
class RatingBase(BaseModel):
    user_id : int
    movie_id: str
    rating: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    
    class Config:
        orm_mode=True


# Comments
class CommentBase(BaseModel):
    user_id : int
    movie_id: str
    comment: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id:int
    class Config:
        orm_mode=True


# MovieList 

class MovieListBase(BaseModel):
    name:str
    author:int
    movies: str 

class MovieListCreate(MovieListBase):
    pass

class MovieList(MovieListBase):
    id:int
    class Config:
        orm_mode = True
    
