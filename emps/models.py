import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobil = PhoneNumberField(null=False, blank=False, unique=True)
    hireDate = models.DateField()

    def __str__(self):
        return self.name


class MinMaxHours(models.FloatField):  # working hours validator (from stackoverflow)
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxHours, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(MinMaxHours, self).formfield(**defaults)


class Attendance(models.Model):
    day = models.DateField(default=datetime.date.today)
    working_hours = MinMaxHours(min_value=0.0, max_value=8.0)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent'),
        ('SICKLEAVE', 'Sick Leave'),
        ('DAYOFF', 'Day OFF'),
    )
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default="Present",
    )

    def __str__(self):
        return self.employee.name
