from django.contrib import admin
from emps.models import Employee, Attendance
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class EmpAttendance(admin.ModelAdmin):
    list_display = ['employee', 'day', 'status', 'working_hours']

    def get_ordering(self, request):
        return [('-day')]


class Emp(admin.ModelAdmin):
    list_display = ['name', 'email', 'mobil', 'hireDate']
    search_fields = ['name']

    def get_ordering(self, request):
        return [('hireDate')]


admin.site.register(Attendance, EmpAttendance)
admin.site.register(Employee, Emp)
admin.site.site_header = "HR Managers"
admin.site.site_title = "HR Emp"
admin.site.index_title = "admin page"
