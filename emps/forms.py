from django.forms import ModelForm, TextInput
from emps.models import Attendance
from django import forms


class AttendanceForm(forms.Form):
    employee = forms.CharField(max_length=100, required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)


class EmployeeForm(forms.Form):
    year = forms.CharField(max_length=4, required=False)
    month = forms.CharField(max_length=2, required=False)
