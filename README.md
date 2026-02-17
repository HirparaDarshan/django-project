# django-project
# Django User Registration System

A complete **Django user registration and profile management system** with a custom user model, profile fields, registration/login functionality, admin integration, and Bootstrap 5 styled templates.

---

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Database](#database)
- [Usage](#usage)
- [Branching Strategy](#branching-strategy)
- [Commit Guidelines](#commit-guidelines)

---

## Features
- **Custom User Model (`CustomUser`)** with email uniqueness  
- **One-to-One Profile (`Profile`)** containing:
  - Mobile number  
  - Hobby  
  - Country  
  - Profile picture (displayed as round avatar like WhatsApp)  
- **One form, two-model architecture** for registration  
- Registration, login, and logout functionality  
- Admin panel integration with **stacked inline Profile editing**  
- **Bootstrap 5 responsive templates**:
  - `home.html` (shows profile info and avatar)  
  - `register.html` (clean, rounded form inputs with placeholders)  
- Media & static file handling (profile pics and CSS/JS)  
- Optimized migrations and signals for automatic Profile creation  

---

## Technologies
- **Python 3.12**  
- **Django 4.2**  
- **MySQL** as the database backend  
- **Bootstrap 5** for front-end styling  
- **HTML, CSS, JS** for templates and forms  

---

## Project Structure
user_registration/
│
├── manage.py
├── MySQL database
├── requirements.txt
├── README.md
├── static/
│ └── user_registration_form/
│ └── css/
│ ├── home.css
│ └── register.css
├── media/
│ └── profile_pics/
├── user_registration/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── user_registration_form/
├── admin.py
├── apps.py
├── forms.py
├── models.py
├── signals.py
├── templates/
│ └── user_registration_form/
│ ├── home.html
│ └── register.html
├── views.py
└── migrations/


---

## Setup & Installation

1. **Clone the repository**
bash
git clone https://github.com/HirparaDarshan/django-project.git
cd django-project

2. Create virtual environment
python -m venv djangoenv
source djangoenv/bin/activate   # Linux/Mac
djangoenv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure database
Update user_registration/settings.py with your MySQL credentials or .env file:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_db_name",
        "USER": "your_db_user",
        "PASSWORD": "your_db_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}

5. Apply migrations
python manage.py makemigrations
python manage.py migrate

6. Create superuser
python manage.py createsuperuser

7. Run the development server
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the project.


# Usage
- Register new users via /register/
- Login via /login/
- Logout via /logout/
- View user profile on home page
- Admin panel: /admin/ to manage users and profiles

# Branching Strategy
- main: stable, production-ready code
- feature/user-auth: registration, login, profile features

# Commit Guidelines
- Add CustomUser & Profile models
- Implement registration/login views & templates
- Integrate Profile inline in admin panel
- Add Bootstrap 5 styling
- Optimize migrations and signals for automatic profile creation
