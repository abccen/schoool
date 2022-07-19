from django.db import models
from school_app.models import School
from django.contrib.auth.models import User
from auth_app.models import MyUser


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=45)
    duration = models.DateField()
    is_active = models.BooleanField()
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='employee', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    M = 'Male'
    F = 'Female'
    GENDER = [
        (M, 'Male'),
        (F, 'Female')
    ]
    gender = models.CharField(max_length=6, choices=GENDER, blank=True, null=True)
    salary = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.phone_number}, {self.user}'
