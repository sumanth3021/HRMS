# Basic HRMS (Human Resource Management System)

## Project Overview
This project is a Basic Human Resource Management System (HRMS) developed using Django.
It allows managing employee information, tracking attendance, and generating simple reports.

The application is designed as part of an intern backend developer assignment to demonstrate
Django fundamentals, ORM usage, API creation, and clean project structure.

---

## Features
- Welcome landing page
- Employee list view
- Add new employee
- View employee details
- Register employee attendance (In Time / Out Time)
- Attendance history per employee
- Department-wise employee count report
- Django Admin panel integration

---

## Tech Stack
- Python 3.x
- Django
- SQLite (default Django database)
- HTML with internal CSS

---

## Project Structure
HRMS_PROJECT/
├── README.md
├── manage.py
├── requirements.txt
├── hrms/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│       └── frontend/
│           ├── welcome.html
│           ├── home.html
│           ├── add_employee.html
│           ├── employee_detail.html
│           ├── add_attendance.html
│           └── department_report.html
└── hrms_project/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py



## How to Run the Project Locally

### 1. Create Virtual Environment
python -m venv venv

### 2. Activate Virtual Environment (Windows)
venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Apply Database Migrations
python manage.py migrate

### 5. Create Admin User (Optional)
python manage.py createsuperuser

### 6. Run Development Server
python manage.py runserver


### 7. Open in Browser
http://127.0.0.1:8000/



---

## Admin Panel
- URL: `http://127.0.0.1:8000/admin/`
- Admin users can manage employees and attendance records

---

## Notes
- The project uses SQLite for simplicity
- Internal CSS is used for basic UI styling
- Proper docstrings are added to models and views
- Code follows Django best practices

---

## Author
Sumanth Polothu
