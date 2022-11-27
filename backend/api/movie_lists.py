
# import json
# from fastapi import FastAPI, APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session

# from .models import models,schemas
# from . import crud
# from ..database import get_db

# router = APIRouter()

# @router.get("/movie_lists/", response_model=list[schemas.MovieList], tags=["movie_lists"])
# def get_movie_lists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     movie_lists = crud.get_movie_lists(db, skip=skip, limit=limit)
#     return movie_lists

# # @router.get("/movie_lists/user", response_model=list[schemas.MovieList], tags=["movie_lists","users"])
# # def get_movie_list_by_user(user_id: int, db: Session = Depends(get_db)):
# #     movie_lists = crud.get_movie_lists_by_user(db, user_id)
# #     return movie_lists

# @router.put("/movie_lists/", response_model=schemas.MovieList, tags=["movie_lists"])
# def update_movie_list(movie_list: schemas.MovieListCreate, db: Session = Depends(get_db)) :
#     db_movie_list = crud.get_movie_list(db, movie_list.id)
#     if not db_movie_list:
#         raise HTTPException(status_code=400, detail=f"MovieList not found in base.")
#     movie_list.movies = json.dumps(movie_list.movies)
#     return crud.update_movie_list(db, movie_list)

# from json import JSONEncoder
# class MyEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__ 

# @router.post("/movie_lists/", response_model=schemas.MovieList, tags=["movie_lists"])
# def add_movie_list(movie_list: schemas.MovieListCreate, db: Session = Depends(get_db)) :
#     movie_list.movies = json.dumps(movie_list.movies,cls=MyEncoder)
#     print(type(movie_list))
#     return crud.create_movie_list(db=db, movie_list=movie_list)

# # ======== DELETE ========

# @router.delete("/movie_lists/", response_model=schemas.MovieList, tags=["movie_lists"])
# def delete_movie_list(movie_list: schemas.MovieList, db: Session = Depends(get_db)):
#     db_movie_list = crud.get_movie_list(db, movie_list.id)
#     if not db_movie_list:
#         raise HTTPException(status_code=400, detail=f"MovieList not found in base.")
#     return crud.remove_movie_list(db=db, movie_list=movie_list)
