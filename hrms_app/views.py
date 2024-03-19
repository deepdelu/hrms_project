from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Attendance
from django.utils import timezone
from django.db.models import Count
from django.db.models import Q


# creating function for the home.html
def home(request):
    employee = Employee.objects.first()
    return render(request, 'hrms_app/home.html', {'employee': employee})

# creating function for the employees.html
def employees(request):
    employees_list = Employee.objects.all()
    return render(request, 'hrms_app/employees.html', {'employees': employees_list})

# creating function for the add_employee.html

def add_employee(request):
    if request.method == 'POST':
        # Retrieve form data from the request
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        date_of_joining = request.POST.get('date_of_joining')

        # Create a new Employee instance and save it to the database
        employee = Employee.objects.create(
            name=name,
            designation=designation,
            department=department,
            date_of_joining=date_of_joining
        )

        # Redirect to the employees list page after adding the employee
        return redirect('employees')
    else:
        return render(request, 'hrms_app/add_employee.html')

# creating function for the mark_attendance.html
def mark_attendance(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
        # Get the selected date from the form
        selected_date = timezone.now().date()  # Assuming you're marking attendance for the current date

        # Loop through each employee and save attendance if it's not already marked for the selected date
        for employee in employees:
            status_key = 'status_' + str(employee.id)
            attendance_status = request.POST.get(status_key)
            if attendance_status:
                # Check if attendance is already marked for the selected date for the current employee
                existing_attendance = Attendance.objects.filter(
                    Q(employee=employee) & Q(attendance_date=selected_date)
                ).exists()
                if not existing_attendance:
                    # If attendance is not marked for the selected date, save the new attendance record
                    attendance = Attendance(employee=employee, attendance_date=selected_date, status=attendance_status)
                    attendance.save()

        return redirect('home')
    else:
        return render(request, 'hrms_app/mark_attendance.html', {'employees': employees})



# creating function for the attendance_details.html
def attendance_details(request):
    employees = Employee.objects.all()
    attendance_records = []
    # Loop through each employee and retrieve their attendance records
    for employee in employees:
        records = Attendance.objects.filter(employee=employee)
        attendance_records.append({'employee': employee, 'attendance_records': records})

    return render(request, 'hrms_app/attendance_details.html', {'attendance_records': attendance_records})


# creating function for the employee_reports.html
def employee_report(request):
    # Get the count of employees in each department
    department_counts = Employee.objects.values('department').annotate(total=Count('department'))
    # Pass the data to the template
    return render(request, 'hrms_app/employee_report.html', {'department_counts': department_counts})

