from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi import Depends,APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status,HTTPException
from backend.api import crud

from backend.database import get_db
from backend.api.core.hashing import Hasher
from backend.api.models.schemas import Token
# from backend.api.users import get_user
from backend.api.core.security import create_access_token
from backend.api.core.config import settings

from jose import JWTError, jwt

router = APIRouter()

def authenticate_user(username: str, password: str,db: Session):
    user = crud.get_user(username=username,db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/login/token", response_model=Token, tags=["auth", "users"])
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),db: Session= Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password,db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"username": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

def get_current_user_from_token(token: str = Depends(oauth2_scheme),db: Session=Depends(get_db)): 
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("username")

        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_user(username=username,db=db)
    if user is None:
        raise credentials_exception
    return user

