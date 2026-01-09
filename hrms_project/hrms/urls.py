from django.urls import path
from . import views

urlpatterns = [
    # Landing page
    path("", views.welcome_page, name="welcome"),

    # Home page (Employee list)
    path("home/", views.home, name="home"),

    # Employee pages
    path("employee/add/", views.add_employee_form, name="add_employee_form"),
    path("employee/<int:emp_id>/", views.employee_detail, name="employee_detail"),

    # Attendance
    path("attendance/add/<int:emp_id>/", views.add_attendance_form, name="add_attendance_form"),

    # Report
    path("report/", views.department_report, name="department_report"),

    # APIs
    path("api/employees/add/", views.add_employee, name="add_employee"),
    path("api/employees/", views.get_employees, name="get_employees"),
    path("api/attendance/add/", views.mark_attendance, name="mark_attendance"),
    path("api/attendance/<int:emp_id>/", views.get_attendance_by_employee, name="get_attendance"),
]
