from django.db import models

class Employee(models.Model):
    """
    Stores employee information.
    """
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name


class Attendance(models.Model):
    """
    Stores attendance details for employees.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    in_time = models.TimeField()
    out_time = models.TimeField()

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
