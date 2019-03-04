from django.contrib import admin
from emps.models import Employee, Attendance
from django.contrib.auth.models import Group

admin.site.unregister(Group)  # remove Group from admin page


# Modify how the Attendance page will look like
class EmpAttendance(admin.ModelAdmin):
    list_display = ['employee', 'day', 'status', 'working_hours']
    search_fields = ['employee__name__icontains', 'day', ]

    def get_ordering(self, request):
        return [('-day')]


class Emp(admin.ModelAdmin):  # Modify how the Employees page will look like
    list_display = ['name', 'email', 'mobil', 'hireDate']
    search_fields = ['name']

    def get_ordering(self, request):
        return [('hireDate')]


admin.site.register(Attendance, EmpAttendance)
admin.site.register(Employee, Emp)
admin.site.site_header = "eSEED HRs"
admin.site.site_title = "HR Emp"
admin.site.index_title = "admin page"
