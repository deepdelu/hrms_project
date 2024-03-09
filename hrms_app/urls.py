# hrms_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employees/', views.employees, name='employees'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('attendance-details/', views.attendance_details, name='attendance_details'),
    path('employee-report/', views.employee_report, name='employee_report'),
    path('add-employee/', views.add_employee, name='add_employee'),
]