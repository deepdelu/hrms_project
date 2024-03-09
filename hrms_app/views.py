from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Attendance
from django.utils import timezone
from django.db.models import Count 
from .forms import *

def home(request):
    employee = Employee.objects.first()
    return render(request, 'hrms_app/home.html', {'employee': employee})

def employees(request):
    employees_list = Employee.objects.all()
    return render(request, 'hrms_app/employees.html', {'employees': employees_list})



def mark_attendance(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        # Loop through each employee and save attendance
        for employee in employees:
            status_key = 'status_' + str(employee.id)  # Construct the name of the status field
            attendance_status = request.POST.get(status_key)  # Get the status for the current employee
            if attendance_status:  # Ensure that a status is provided
                attendance = Attendance(employee=employee, attendance_date=timezone.now(), status=attendance_status)
                attendance.save()
        return redirect('home')  # Redirect to home page after marking attendance
    else:
        return render(request, 'hrms_app/mark_attendance.html', {'employees': employees})



def attendance_details(request):
    employees = Employee.objects.all()
    attendance_records = []
    # Loop through each employee and retrieve their attendance records
    for employee in employees:
        records = Attendance.objects.filter(employee=employee)
        attendance_records.append({'employee': employee, 'attendance_records': records})

    return render(request, 'hrms_app/attendance_details.html', {'attendance_records': attendance_records})



def employee_report(request):
    # Get the count of employees in each department
    department_counts = Employee.objects.values('department').annotate(total=Count('department'))
    # Pass the data to the template
    return render(request, 'hrms_app/employee_report.html', {'department_counts': department_counts})


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees')  # Redirect to employees list page after adding employee
    else:
        form = EmployeeForm()
    return render(request, 'hrms_app/add_employee.html', {'form': form})