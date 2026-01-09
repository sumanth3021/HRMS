from django.contrib import admin
from .models import Employee, Attendance


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """
    Admin configuration for Employee model.
    """
    list_display = ("name", "designation", "department", "email", "date_of_joining")
    search_fields = ("name", "email", "department")
    list_filter = ("department",)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """
    Admin configuration for Attendance model.
    """
    list_display = ("employee", "date", "in_time", "out_time")
    list_filter = ("date",)

