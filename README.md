# BlogApp

A complete, functional, and beautifully styled Django web application designed for learning purposes and future Docker containerization.

## Features

- **User Module**: User registration, login, logout, and profile page. Normal users must be authenticated to create, edit, or delete posts. Users can only edit or delete their own posts.
- **Blog Module**: Home page listing all blog posts (newest first), detail page, create, edit, and delete functionalities. Uses Django ModelForms and flash messages.
- **Admin Module**: Standard Django admin access and a custom staff-only Dashboard containing total metrics, latest users, latest posts, and user/post deletion capabilities.
- **Responsive UI**: Premium styling utilizing Bootstrap 5, glassmorphism headers, dynamic success/error alerts, and cohesive typography.

## Technology Stack

- Python
- Django
- SQLite
- HTML5 / CSS3 / Bootstrap 5
- Django Template Engine

## Local Setup Instructions

Follow these steps to run the application locally:

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

- **Windows (PowerShell)**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **Windows (CMD)**:
  ```cmd
  .\venv\Scripts\activate.bat
  ```
- **macOS / Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser / Staff User

To access the custom admin dashboard, create an administrator user:

```bash
python manage.py createsuperuser
```

### 6. Run Django Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.
