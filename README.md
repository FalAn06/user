{
  "id": 1,
  "username": "new_user",
  "email": "user@example.com",
  "created_at": "2025-07-01T12:34:56",
  "updated_at": "2025-07-01T12:34:56"
}
Respuesta exitosa:
{
  "id": 1,
  "username": "new_user",
  "email": "new_user@example.com",
  "created_at": "2025-07-01T12:34:56",
  "updated_at": "2025-07-01T12:34:56"
}

2. login-user: Autenticación de usuarios
Este microservicio gestiona el inicio de sesión de los usuarios. Si las credenciales son correctas, genera un JSON Web Token (JWT) que el usuario puede utilizar para acceder a otros recursos protegidos dentro del sistema.

Endpoint:
POST /users/login

Parámetros:
username (str): Nombre de usuario.

password (str): Contraseña del usuario.

Ejemplo de solicitud:
{
  "username": "new_user",
  "password": "securepassword123"
}

Respuesta exitosa:
{
  "id": 1,
  "username": "new_user",
  "email": "new_user@example.com",
  "created_at": "2025-07-01T12:34:56",
  "updated_at": "2025-07-01T12:34:56",
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsImV4cCI6MTc1MjM2OTAzNH0.WsNikj6XDKURYMa7VhSZKA0pdRmULW5qZbW2edC4cJE"
}
3. update-user: Actualización de usuario
Este microservicio permite a los usuarios actualizar su información (nombre de usuario, correo electrónico) y cambiar su contraseña. La contraseña solo puede cambiarse si la contraseña actual proporcionada es correcta.

Endpoints:
PUT /users/update: Actualiza los datos básicos del usuario.

PUT /users/change-password: Cambia la contraseña del usuario.

Parámetros:
Para actualizar datos:

id (int): ID del usuario.

username (str): Nuevo nombre de usuario.

email (str): Nuevo correo electrónico.

Para cambiar la contraseña:

id (int): ID del usuario.

old_password (str): Contraseña actual.

new_password (str): Nueva contraseña.

Ejemplo de solicitud para actualizar datos:
{
  "id": 1,
  "username": "updated_user",
  "email": "updated_email@example.com"
}

Ejemplo de solicitud para cambiar la contraseña:
{
  "id": 1,
  "old_password": "securepassword123",
  "new_password": "newsecurepassword456"
}

Respuesta exitosa para actualización de datos:
{
  "id": 1,
  "username": "updated_user",
  "email": "updated_email@example.com",
  "created_at": "2025-07-01T12:34:56",
  "updated_at": "2025-07-01T12:45:00"
}

Instalación y Ejecución del Proyecto
1. Clona el repositorio:
git clone <url-del-repositorio>
cd <nombre-del-repositorio>

2. Configura un entorno virtual:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Instala las dependencias:
pip install -r requirements.txt

5. Ejecuta el microservicio:
uvicorn src.main:app --reload --host 127.0.0.1 --port 8001

Conclusión
Este repositorio contiene los microservicios para el manejo básico de usuarios en una aplicación. Hemos cubierto el registro, inicio de sesión y la actualización de usuarios, con la seguridad que provee el uso de contraseñas encriptadas y tokens JWT.

