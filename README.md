# ToDo List API

A RESTful API for managing personal tasks, built with Django REST Framework. Users can register, log in, and manage their own tasks — organized into categories, with filtering and search support.

## Features

- JWT authentication (register, login, token refresh)
- Full CRUD for tasks and categories
- Each user can only access their own data
- Filter tasks by category, completion status, or due date
- Search tasks by title/description
- Order tasks by due date or creation date
- Paginated responses
- Interactive API documentation (Swagger UI)

## Tech Stack

- Python 3 / Django / Django REST Framework
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- `django-filter` for filtering/search
- `drf-spectacular` for API documentation

## Setup Instructions

1. Clone the repository
git clone https://github.com/fredrickmwendwa/todo-list-api.git
cd todo-list-api

2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Create a PostgreSQL database and update your `.env` file (see `.env.example`)

5. Run migrations
python manage.py migrate

6. Start the server
python manage.py runserver

7. Visit `http://127.0.0.1:8000/api/docs/` for interactive API documentation

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Log in and receive JWT tokens |
| POST | `/api/auth/login/refresh/` | Refresh an access token |
| GET/POST | `/api/categories/` | List or create categories |
| GET/PUT/PATCH/DELETE | `/api/categories/{id}/` | Manage a single category |
| GET/POST | `/api/tasks/` | List or create tasks |
| GET/PUT/PATCH/DELETE | `/api/tasks/{id}/` | Manage a single task |

### Filtering & Search

- `/api/tasks/?category=1`
- `/api/tasks/?is_completed=true`
- `/api/tasks/?search=keyword`
- `/api/tasks/?ordering=due_date`