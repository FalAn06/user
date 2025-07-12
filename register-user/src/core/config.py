from pydantic_settings import BaseSettings

from dotenv import load_dotenv
import os

# Cargar el archivo .env
load_dotenv()

class Settings(BaseSettings):
    # Base de datos
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))  # Valor por defecto 5432
    DB_NAME: str = os.getenv("DB_NAME")
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    class Config:
        env_file = ".env"

# Instanciamos el objeto de configuración
settings = Settings()
