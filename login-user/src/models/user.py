# src/models/user.py

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.core.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    # Definición de las columnas
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relación con otras tablas (si es necesario)
    # Esta relación puede variar dependiendo de cómo diseñes tu modelo de datos

    def __repr__(self):
        return f"<User {self.username}>"
