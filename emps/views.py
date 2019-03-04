from django.shortcuts import render
from django import forms
from emps.forms import AttendanceForm
from emps.models import Attendance


def home(request):
    form = AttendanceForm()
    empname = request.GET.get('employee')
    startdate = request.GET.get('start_date')
    enddate = request.GET.get('end_date')
    empdata = []
    result = 0
    if empname and not startdate and not enddate:
        empdata = Attendance.objects.filter(employee__name__icontains=empname)
    else:
        empdata = Attendance.objects.filter(
            employee__name__icontains=empname).filter(day__range=[startdate, enddate])
    if empdata:
        for emp in empdata:
            result += emp.working_hours
    context = {
        'form': form,
        'empdata': empdata,
        'start': startdate,
        'end': enddate,
        'totalworkinghours': result
    }

    return render(request, "emps/home.html", context)
