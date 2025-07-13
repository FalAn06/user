from pydantic import BaseModel

class UserUpdate(BaseModel):
    id: int
    username: str
    email: str
    old_password: str = None  # Solo se necesita en el cambio de contraseña
    new_password: str = None  # Solo se necesita en el cambio de contraseña

    class Config:
        orm_mode = True
