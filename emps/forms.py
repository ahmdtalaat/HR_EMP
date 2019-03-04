from django.forms import ModelForm, TextInput
from emps.models import Attendance
from django import forms


class AttendanceForm(forms.Form):
    employee = forms.CharField(max_length=100, required=True)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
