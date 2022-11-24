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

# User
class UserBase(BaseModel):
    id:int

class UserCreate(UserBase):
    pass

class User(UserBase):
    class Config:
        orm_mode = True

# Rating
class RatingBase(BaseModel):
    user_id : int
    movie_title: str
    movie_year: int
    rating: int

class RatingCreate(RatingBase):
    pass

class Rating(RatingBase):
    
    class Config:
        orm_mode=True


# Comments
class CommentBase(BaseModel):
    user_id : int
    movie_title: str
    movie_year: int
    comment: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    
    class Config:
        orm_mode=True

    