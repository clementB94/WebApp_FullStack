from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db, engine
from .. import scraping

router = APIRouter()

# ======== GET ========
@router.get("/users/", response_model=list[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
# @router.get("/users/{id}", response_model=schemas.User)
# def get_user_by_id(id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_id(db, id=id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail=f"User {id} not found")
#     return db_user

# ======== POST ========

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_id(db, title=user.id)
    # if db_user:
    #     raise HTTPException(status_code=400, detail=f"User {user.id} already in base.")
    return crud.create_user_init(db=db, user=user)