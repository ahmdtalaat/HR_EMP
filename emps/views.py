from django.shortcuts import render
from django import forms
from emps.forms import AttendanceForm, EmployeeForm
from emps.models import Attendance, Employee
from django.db.models import Avg


def home(request):
    form = AttendanceForm(request.GET)
    empname = request.GET.get('employee')
    startdate = request.GET.get('start_date')
    enddate = request.GET.get('end_date')
    empdata = []
    result = 0
    if not empname and not startdate and not enddate:
        empdata = []
    elif empname and not startdate and not enddate:
        empdata = Attendance.objects.filter(
            employee__name__icontains=empname).order_by('-day')
    else:
        empdata = Attendance.objects.filter(
            employee__name__icontains=empname).filter(day__range=[startdate, enddate]).order_by('-day')
    if empdata:
        for emp in empdata:
            result += emp.working_hours
        result = round(result, 2)
    context = {
        'form': form,
        'empdata': empdata,
        'start': startdate,
        'end': enddate,
        'totalworkinghours': result
    }

    return render(request, "emps/home.html", context)


def empofthemonth(request):
    form = EmployeeForm(request.GET)
    year = request.GET.get('year')
    month = request.GET.get('month')
    all_emps = Employee.objects.all()
    allempofmon = {}
    emp_of_month = {}
    if year and month:
        for emp in all_emps:
            allempofmon[emp.name] = Attendance.objects.filter(day__year=year, day__month=month).filter(
                employee=emp).aggregate(Avg('working_hours'))['working_hours__avg']
    else:
        allempofmon = {}
    if allempofmon:
        for emp in allempofmon:
            if allempofmon[emp] is not None:
                if allempofmon[emp] >= 7:
                    emp_of_month[emp] = round(allempofmon[emp], 2)
    else:
        emp_of_month = {}
    return render(request, "emps/about.html", {'allempofmonth': emp_of_month, 'form': form})
