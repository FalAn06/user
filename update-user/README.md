# Update User Microservice

This microservice provides the functionality to update user details and change their password. It is built using FastAPI and connects to a PostgreSQL database for data persistence. The microservice provides two main endpoints:

- **Update User**: Update user details like username and email.
- **Change Password**: Update a user's password after verifying the old password.

## Features

- **Update user details** (username and email).
- **Change password** after verifying the old password.
- Uses JWT for authentication.

## Technologies Used

- **FastAPI**: Web framework for building APIs.
- **SQLAlchemy**: ORM for database operations.
- **Pydantic**: Data validation and settings management.
- **PostgreSQL**: Database for storing user information.
- **Python-Jose**: Handling JWT (JSON Web Tokens) for secure authentication.
- **Uvicorn**: ASGI server for running the FastAPI application.
- **PassLib**: Password hashing and verification.

## Installation

Follow the steps below to get the microservice running locally:

### Prerequisites

1. Python 3.9 or higher.
2. PostgreSQL running locally or in the cloud.
3. Install necessary dependencies.

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/update-user-microservice.git


Navigate to the project directory:

cd update-user-microservice

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

pip install -r requirements.txt

Create a .env file in the root directory with the following configuration:
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database_name
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

Run the application:

uvicorn src.main:app --reload --host 127.0.0.1 --port 8002

API Endpoints
PUT /users/update
Update the user's information (username and email).

Request Body:

{
  "id": 4,
  "username": "newUsername",
  "email": "newemail@example.com"
}

Response:
{
  "message": "User updated successfully"
}

PUT /users/change-password
Change the user's password after verifying the old password.

Request Body:

{
  "id": 4,
  "username": "testuser",
  "email": "testuser@example.com",
  "old_password": "currentpassword123",
  "new_password": "newpassword123"
}

Response:
{
  "message": "Password updated successfully"
}

Authentication
This microservice uses JWT (JSON Web Tokens) for user authentication. You need to provide a valid token in the Authorization header when making requests to the protected endpoints.

Testing with Postman
Update User: Make a PUT request to http://127.0.0.1:8002/users/update with the necessary JSON body.

Change Password: Make a PUT request to http://127.0.0.1:8002/users/change-password with the current and new password.
