# Django/Flask Web API Project

This project is a Django-based Web API with CRUD operations for Todo items and user authentication.

## Features

- User registration and login
- JWT token-based authentication
- Todo item CRUD operations

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Other dependencies (see requirements.txt)

### Installation

1. Clone the repository:

    ```bash
    cd your-project
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### AuthController

- POST `/auth/register/`: Register a new user.
- POST `/auth/login/`: Log in and obtain a JWT token.

### TodoController

- GET `/todo/getall/`: Get all Todo items.
- GET `/todo/get/{id}/`: Get a specific Todo item.
- POST `/todo/create/`: Create a new Todo item.
- PUT `/todo/put/{id}/`: Update a Todo item.
- DELETE `/todo/delete/{id}/`: Delete a Todo item.

## Authors

- Rohit Patel