import os
# from dotenv import load_dotenv

# from pathlib import Path
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Web App Movies"
    PROJECT_VERSION: str = "1.0.0"
    
    # SECRET_KEY :str = os.getenv("SECRET_KEY")   
    SECRET_KEY :str = "secretkey"   #Temporaire 
    ALGORITHM = "HS256"                       
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  #in mins 

settings = Settings()
