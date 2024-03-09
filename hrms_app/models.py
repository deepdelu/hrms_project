from django.db import models

# creating employee model to store all data of employees
class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name

# creating attendance model to take attendance record of employees
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.employee.name} - {self.attendance_date} - {self.status}"
