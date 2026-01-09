from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count

def home(request):
    """
    Displays the list of all employees on the home page.
    """
    employees = Employee.objects.all()
    return render(request, "frontend/home.html", {"employees": employees})


@csrf_exempt
def add_employee(request):
    """
    API endpoint to add a new employee.
    """
    if request.method == "POST":
        data = json.loads(request.body)

        Employee.objects.create(
            name=data.get("name"),
            designation=data.get("designation"),
            department=data.get("department"),
            email=data.get("email"),
            date_of_joining=data.get("date_of_joining"),
        )

        return JsonResponse({"message": "Employee added successfully"})

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


def get_employees(request):
    """
    API endpoint to retrieve all employees.
    """
    employees = Employee.objects.all()
    data = list(employees.values())
    return JsonResponse(data, safe=False)

# Attendance.

from .models import Attendance
from django.shortcuts import get_object_or_404


@csrf_exempt
def mark_attendance(request):
    """
    API endpoint to mark attendance for a specific employee.
    """
    if request.method == "POST":
        data = json.loads(request.body)

        employee = get_object_or_404(Employee, id=data.get("employee_id"))

        Attendance.objects.create(
            employee=employee,
            date=data.get("date"),
            in_time=data.get("in_time"),
            out_time=data.get("out_time"),
        )

        return JsonResponse({"message": "Attendance marked successfully"})

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


def get_attendance_by_employee(request, emp_id):
    """
    API endpoint to retrieve attendance details for a specific employee.
    """
    records = Attendance.objects.filter(employee_id=emp_id)

    data = list(records.values("date", "in_time", "out_time"))

    return JsonResponse(data, safe=False)



def employee_detail(request, emp_id):
    """
    Displays employee details along with attendance records.
    """
    employee = get_object_or_404(Employee, id=emp_id)
    attendance_records = Attendance.objects.filter(employee=employee)

    return render(
        request,
        "frontend/employee_detail.html",
        {
            "employee": employee,
            "attendance_records": attendance_records,
        },
    )
    
    
    
#  Add Employee
def add_employee_form(request):
    """
    Displays and handles add employee form.
    """
    error = None

    if request.method == "POST":
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        department = request.POST.get("department")
        email = request.POST.get("email")
        date_of_joining = request.POST.get("date_of_joining")

        # Simple validation
        if not all([name, designation, department, email, date_of_joining]):
            error = "All fields are required."
        else:
            Employee.objects.create(
                name=name,
                designation=designation,
                department=department,
                email=email,
                date_of_joining=date_of_joining,
            )
            return redirect("/home/")

    return render(
        request,
        "frontend/add_employee.html",
        {"error": error}
    )





# Attendance

def add_attendance_form(request, emp_id):
    """
    Displays and handles attendance form.
    """
    employee = get_object_or_404(Employee, id=emp_id)

    if request.method == "POST":
        Attendance.objects.create(
            employee=employee,
            date=request.POST.get("date"),
            in_time=request.POST.get("in_time"),
            out_time=request.POST.get("out_time"),
        )
        return redirect(f"/employee/{emp_id}/")

    return render(
        request,
        "frontend/add_attendance.html",
        {"employee": employee}
    )





def department_report(request):
    """
    Displays the count of employees in each department.
    """
    report_data = (
        Employee.objects
        .values("department")
        .annotate(count=Count("id"))
    )

    return render(
        request,
        "frontend/department_report.html",
        {"report_data": report_data}
    )


# Welcome

def welcome_page(request):
    """
    Displays welcome landing page.
    """
    return render(request, "frontend/welcome.html")
