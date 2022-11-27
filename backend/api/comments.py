
from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db

router = APIRouter()

@router.get("/comments/", response_model=list[schemas.Comment], tags=["comments"])
def get_comments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = crud.get_comments(db, skip=skip, limit=limit)
    return comments

@router.get("/comments/{id}", response_model=list[schemas.Comment], tags=["comments"])
def get_comments(id:int, db: Session = Depends(get_db)):
    comments = crud.get_comment(db, id)
    return comments

@router.get("/comments/user/", response_model=list[schemas.Comment], tags=["comments","users"])
def get_comment_by_user(username: str, db: Session = Depends(get_db)):
    comments = crud.get_comments_by_user(db, username)
    return comments

@router.get("/comments/movie/", response_model=list[schemas.Comment], tags=["comments","movies"])
def get_comment_by_movie(movie_id: str, db: Session = Depends(get_db)):
    comments = crud.get_comments_by_movie(db, movie_id)
    return comments

@router.post("/comments/", response_model=schemas.Comment, tags=["comments"])
def add_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)) :
    # db_comment = crud.get_comment(db, comment.id)
    # if db_comment:
    #     return crud.update_comment(db=db, comment=comment)
    return crud.create_comment(db=db, comment=comment)

# ======== DELETE ========

@router.delete("/comments/", response_model=schemas.Comment, tags=["comments"])
def delete_comment(comment: schemas.Comment, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment.movie_id, comment.username)
    if not db_comment:
        raise HTTPException(status_code=400, detail=f"Comment not found in base.")
    return crud.remove_rating(db=db, comment=comment)