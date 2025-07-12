# 📦 Register User Microservice

Este microservicio está diseñado para permitir el **registro de usuarios** en una plataforma. Permite crear una cuenta proporcionando un **nombre de usuario**, **correo electrónico** y **contraseña**.  
Valida que el correo y el nombre de usuario no estén registrados, encripta la contraseña y devuelve la información del nuevo usuario (sin exponer la contraseña).

---

## ✅ Requisitos

- Python 3.9 o superior  
- PostgreSQL  
- pip

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

2. Crea y activa un entorno virtual
En Windows (PowerShell)

python -m venv venv
.\venv\Scripts\Activate.ps1

3. Instala las dependencias

pip install -r requirements.txt

🚀 Ejecutar el Servidor
uvicorn src.main:app --reload

Esto iniciará el servidor en:http://127.0.0.1:8000

📌 Endpoint Disponible
POST /users/register
Permite registrar un nuevo usuario.

Cuerpo de la solicitud (JSON)

{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "securepassword123"
}
Respuesta exitosa
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com",
  "created_at": "2025-07-12T12:00:00",
  "updated_at": "2025-07-12T12:00:00"
}
Errores comunes
400: Usuario o correo ya registrados.

422: Datos inválidos o campos faltantes.
{
  "detail": "Username already registered"
}

🗃️ Estructura de la Base de Datos
La tabla users tiene la siguiente estructura:

| Campo             | Tipo      | Restricciones    |
| ----------------- | --------- | ---------------- |
| `id`              | INTEGER   | Primary Key      |
| `username`        | VARCHAR   | Unique, Not Null |
| `email`           | VARCHAR   | Unique, Not Null |
| `hashed_password` | VARCHAR   | Not Null         |
| `created_at`      | TIMESTAMP | Default: now()   |
| `updated_at`      | TIMESTAMP | Default: now()   |


🧱 Arquitectura del Proyecto
Este microservicio sigue una arquitectura modular que facilita la escalabilidad y el mantenimiento. Utiliza:

FastAPI: Framework para construir APIs rápidas.

SQLAlchemy: ORM para la base de datos.

Pydantic: Validación de entrada y salida.

Passlib + bcrypt: Encriptación segura de contraseñas.

PostgreSQL: Motor de base de datos relacional.

🔄 Estilo de Arquitectura
El microservicio utiliza arquitectura RESTful, permitiendo comunicación clara vía HTTP usando los métodos GET, POST, PUT, DELETE, etc.


🧠 Patrones y Principios
Patrones
MVC (Modelo-Vista-Controlador):

Modelo: SQLAlchemy

Vista: JSON a través de FastAPI

Controlador: Endpoints definidos en la API

Singleton: Se maneja una única instancia de conexión a la base de datos.

Principios
SOLID: Código modular, flexible y mantenible.

DRY (Don't Repeat Yourself): Reutilización del código evitando duplicación.

📝 Notas Finales
Asegúrate de que el servidor de PostgreSQL esté corriendo antes de ejecutar el microservicio.

Si tienes problemas con las dependencias, elimina el entorno virtual y créalo nuevamente:

