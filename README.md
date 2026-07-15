# Dockerized Django Blog Platform

A production-style Django blog application built with Docker, Docker Compose, MySQL, Gunicorn, and Nginx. The project demonstrates modern web application deployment practices along with user authentication, blog management, and containerized infrastructure.

---

## Features

### User Module
- User registration, login, and logout
- User profile page
- Authentication required for creating, editing, and deleting posts
- Users can only modify their own blog posts

### Blog Module
- Home page displaying all blog posts
- Blog detail page
- Create, Edit, and Delete blog posts
- Django ModelForms
- Success and error flash messages

### Admin Module
- Django Admin Panel
- Custom staff-only dashboard
- View total users and posts
- View latest registered users
- View latest blog posts
- Delete users and posts from dashboard

### Production Features
- Dockerized application
- Multi-container architecture using Docker Compose
- MySQL database
- Gunicorn WSGI server
- Nginx reverse proxy
- Environment variable configuration using `.env`
- Automatic database migrations during container startup

---

# Architecture

```text
                 Browser
                     │
                     ▼
            Nginx (Port 80)
                     │
                     ▼
         Gunicorn (Port 8000)
                     │
                     ▼
                 Django App
                     │
                     ▼
                  MySQL 8.4
```

---

# Tech Stack

### Backend

- Python 3.12
- Django 5.2

### Database

- MySQL 8.4

### DevOps

- Docker
- Docker Compose
- Gunicorn
- Nginx

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- Django Template Engine

---

# Project Structure

```text
blog-project/
│
├── accounts/
├── blog/
├── config/
├── templates/
├── static/
│
├── nginx/
│   └── default.conf
│
├── compose.yaml
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
├── manage.py
├── .env.example
└── README.md
```

---

# Getting Started

## 1. Clone Repository

```bash
git clone <repository-url>

cd blog-project
```

---

## 2. Create Environment File

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-secret-key

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=blogdb
DB_USER=bloguser
DB_PASSWORD=blogpassword
DB_HOST=db
DB_PORT=3306

DB_ROOT_PASSWORD=rootpassword
```

---

## 3. Build Containers

```bash
docker compose up --build
```

The application will automatically:

- Build the Docker image
- Start MySQL
- Wait until MySQL is healthy
- Run Django migrations
- Start Gunicorn
- Serve the application through Nginx

---

## 4. Access Application

Open:

```
http://localhost
```

---

# Docker Services

| Service | Purpose |
|----------|---------|
| Nginx | Reverse Proxy |
| Gunicorn | WSGI Application Server |
| Django | Web Application |
| MySQL | Database |

---

# Environment Variables

| Variable | Description |
|----------|-------------|
| SECRET_KEY | Django Secret Key |
| DEBUG | Enable Debug Mode |
| ALLOWED_HOSTS | Allowed Hosts |
| DB_NAME | MySQL Database |
| DB_USER | MySQL Username |
| DB_PASSWORD | MySQL Password |
| DB_HOST | MySQL Host |
| DB_PORT | MySQL Port |
| DB_ROOT_PASSWORD | MySQL Root Password |

---

# DevOps Concepts Demonstrated

- Docker Image Creation
- Multi-Container Applications
- Docker Compose
- Docker Networking
- Docker Volumes
- Environment Variables
- Gunicorn WSGI Server
- Nginx Reverse Proxy
- MySQL Container
- Automatic Database Migration
- Health Checks
- Container Startup Automation

---

# Future Improvements

- GitHub Actions CI Pipeline
- AWS EC2 Deployment
- HTTPS with Let's Encrypt
- Monitoring with Prometheus & Grafana
- Kubernetes Deployment

---

# License

This project is created for learning, portfolio, and DevOps practice purposes.