from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserCreate, UserResponse
from src.core.database import get_db
from src.utils.hashing import get_password_hash

router = APIRouter()

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica si ya existe un usuario con el mismo correo
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Verifica si ya existe un usuario con el mismo nombre de usuario
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Crear el nuevo usuario con la contraseña encriptada
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    # Devolvemos el usuario sin la contraseña
    return db_user
