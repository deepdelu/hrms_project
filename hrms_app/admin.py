from django.contrib import admin
from .models import *
# Register your models here.

# register model Employee
admin.site.register(Employee)
# register model Attendance
admin.site.register(Attendance)