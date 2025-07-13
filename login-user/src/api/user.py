from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserLogin, UserResponse
from src.core.database import get_db
from src.utils.hashing import verify_password
from src.utils.jwt import create_access_token  # Importamos la función para generar el token JWT
from datetime import timedelta
from src.core.config import settings

router = APIRouter()

@router.post("/login", response_model=UserResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Verifica si el usuario existe en la base de datos
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Verifica si la contraseña es correcta
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Generamos el token JWT
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.username}, expires_delta=access_token_expires)

    # Convertimos el usuario a un diccionario compatible con el modelo de Pydantic UserResponse
    user_data = UserResponse(
        id=db_user.id,
        username=db_user.username,
        email=db_user.email,
        created_at=db_user.created_at,
        updated_at=db_user.updated_at
    )

    # Depuración: Verifica si el token está siendo incluido en la respuesta
    response = {**user_data.dict(), "access_token": access_token}
    print(f"Respuesta generada: {response}")

    # Devolvemos el usuario y el token
    return response

