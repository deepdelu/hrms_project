from django import forms
from .models import Employee

# creating form to add employees
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'designation', 'department', 'date_of_joining']

