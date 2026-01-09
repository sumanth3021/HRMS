# HRMS
# 🧑‍💼 Basic HRMS (Human Resource Management System)

A simple **HRMS web application** built using **Django**, designed to manage employees, track attendance, and generate basic reports.  
This project was developed as part of a **Backend Developer Intern assignment**.

---

## 🚀 Features

- Welcome landing page
- View employee list
- Add new employees
- View employee details
- Register employee attendance (In Time / Out Time)
- Attendance history per employee
- Department-wise employee count report
- Django Admin panel integration
- Clean UI with internal CSS and transitions

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (default Django database)
- **Frontend:** HTML with internal CSS
- **ORM:** Django ORM

---
## 📁 Project Structure
HRMS_PROJECT/
├── README.md
├── manage.py
├── requirements.txt
├── hrms/
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── migrations/
│ └── templates/
│ └── frontend/
│ ├── welcome.html
│ ├── home.html
│ ├── add_employee.html
│ ├── employee_detail.html
│ ├── add_attendance.html
│ └── department_report.html
└── hrms_project/
├── settings.py
├── urls.py
├── asgi.py
└── wsgi.py


---

## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/hrms-django.git
cd hrms-django

2️⃣ Create virtual environment
python -m venv venv

3️⃣ Activate virtual environment
venv\Scripts\activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Apply database migrations
python manage.py migrate

6️⃣ Create admin user (optional)
python manage.py createsuperuser

7️⃣ Run development server
python manage.py runserver

8️⃣ Open in browser
http://127.0.0.1:8000/

---
This project was developed to demonstrate backend development skills using Django, including ORM usage, API development, and clean project structure.








