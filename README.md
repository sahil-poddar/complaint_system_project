# Complaint Management System

A web-based complaint management system built with Django, where students can submit complaints and administrators can review, track, and resolve them through a dedicated dashboard.

## Features

- Students can submit complaints through a simple web form
- Students can view the status of their submitted complaints
- Admin dashboard to view, manage, and update complaint status
- Status tracking (e.g., Pending, In Progress, Resolved)
- User authentication for students and admins

## Tech Stack

- Backend: Python, Django
- Database: SQLite
- Frontend: HTML, CSS (Django templates)

## Getting Started

1. Clone the repository
   git clone https://github.com/sahil-poddar/complaint_system_project.git
   cd complaint_system_project

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Apply migrations
   python manage.py migrate

5. Create a superuser
   python manage.py createsuperuser

6. Run the server
   python manage.py runserver

7. Visit http://127.0.0.1:8000/

## Author

Sahil Poddar
