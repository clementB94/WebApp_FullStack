from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .models import models,schemas
from . import crud
from ..database import get_db, engine
from .. import scraping
from .login import get_current_user_from_token
from backend.api.core.hashing import Hasher

router = APIRouter()

# ======== GET ========
@router.get("/users/", response_model=list[schemas.User], tags=["users"])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/{id}", response_model=schemas.User)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    return db_user

@router.get("/users/name/", response_model=schemas.User)
def get_user_by_name(name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, name)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User {id} not found")
    return db_user

@router.get("/users/token/test")
def test_user_auth(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user_from_token)):
    if id == current_user.id:
        return {"msg":"Auth réussie"}
    raise HTTPException(status_code=401,
                            detail=f"Wrong user")


# ======== POST ========

@router.post("/users/", response_model=schemas.User, tags=["users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail=f"User {user.name} already in base. (id {user.id})")
    
    hashed_pwd = Hasher.get_password_hash(user.password)
    user = schemas.UserInDB(**{**user.dict(), "hashed_password":hashed_pwd})
    return crud.create_user(db=db, user=user)