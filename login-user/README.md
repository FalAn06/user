# Login User Microservice

Este microservicio proporciona una API para la autenticación de usuarios mediante **nombre de usuario** y **contraseña**. Si las credenciales son válidas, se genera un **token JWT** para acceder a las rutas protegidas de la aplicación.

## Requisitos

Antes de ejecutar el microservicio, asegúrate de tener las siguientes dependencias instaladas:

- **Python 3.9+**
- **pip** (gestor de paquetes de Python)

## Instalación

1. **Clona el repositorio** (si aún no lo has hecho):

   ```bash
   git clone https://github.com/tu-repositorio/login-user.git
   cd login-user

Crea y activa un entorno virtual:

python3 -m venv venv
source venv/bin/activate
Instala las dependencias:
pip install -r requirements.txt

Configura tu archivo .env con los parámetros correctos:

DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Ejecutar el microservicio
Para ejecutar el microservicio, utiliza el siguiente comando:

uvicorn src.main:app --reload --host 127.0.0.1 --port 8001

Rutas de la API
POST /login
Este endpoint permite a un usuario autenticarse con su nombre de usuario y contraseña. Si las credenciales son correctas, se devuelve un token JWT que puede ser utilizado para acceder a otras rutas protegidas de la API.

URL: /users/login

Método: POST

Cuerpo de la solicitud (JSON):

{
  "username": "testuser",
  "password": "testpassword"
}


Respuesta Exitosa (200 OK):

{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "created_at": "2025-07-13T12:00:00",
  "updated_at": "2025-07-13T12:00:00",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTc1MjM2OTAzNH0.WsNikj6XDKURYMa7VhSZKA0pdRmULW5qZbW2edC4cJE"
}

Respuesta de Error (400 Bad Request):

Si las credenciales son incorrectas o el usuario no existe:

{
  "detail": "Invalid credentials"
}

Estructura de Archivos
La estructura del microservicio es la siguiente:

login-user/
│
├── src/
│   ├── api/
│   │   └── user.py        # Contiene las rutas del microservicio
│   ├── core/
│   │   ├── config.py      # Configuración de la base de datos y JWT
│   │   └── database.py    # Conexión y sesión de la base de datos
│   ├── models/
│   │   └── user.py        # Modelo de usuario para la base de datos
│   ├── schemas/
│   │   └── user.py        # Esquemas de Pydantic para validación de datos
│   ├── utils/
│   │   ├── hashing.py     # Funciones para el manejo de contraseñas
│   │   └── jwt.py         # Funciones para la generación de JWT
│   └── main.py            # Inicia la aplicación FastAPI
├── requirements.txt       # Dependencias del proyecto
├── .env                   # Configuración del entorno
└── README.md              # Este archivo

Dependencias
FastAPI: Framework para crear APIs de forma rápida y eficiente.

Uvicorn: Servidor ASGI para FastAPI.

SQLAlchemy: ORM para interactuar con la base de datos.

Pydantic: Librería para la validación de datos.

Passlib: Librería para manejar el hashing de contraseñas.

python-jose: Librería para trabajar con JSON Web Tokens (JWT).

python-dotenv: Cargar variables de entorno desde un archivo .env.

Notas adicionales:
Asegúrate de que tu base de datos esté correctamente configurada antes de ejecutar el servicio.

El token JWT generado es válido por 30 minutos (configurable en el archivo .env).