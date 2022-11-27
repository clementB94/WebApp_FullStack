import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"
    
    ....
    ....
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY :str = os.getenv("SECRET_KEY")   #new
    ALGORITHM = "HS256"                         #new
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  #in mins  #new

settings = Settings()
