from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.models.user import User
from src.schemas.user import UserUpdate
from src.core.database import get_db
from src.utils.hashing import verify_password, get_password_hash
from datetime import datetime

router = APIRouter()

@router.put("/update-profile", response_model=UserUpdate)
def update_profile(user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.username = user.username
    db_user.email = user.email
    db_user.updated_at = datetime.utcnow()  # Generar fecha de actualización dinámicamente

    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/change-password", response_model=UserUpdate)
def change_password(user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user.id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verifica que la contraseña actual es correcta
    if not verify_password(user.old_password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    # Si es correcta, actualiza la nueva contraseña
    db_user.hashed_password = get_password_hash(user.new_password)
    db_user.updated_at = datetime.utcnow()  # Generar fecha de actualización dinámicamente

    db.commit()
    db.refresh(db_user)
    return db_user
