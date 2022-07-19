from django.db import models
from courses_app.models import Course


class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=14)
    email = models.EmailField()
    gender = models.CharField(max_length=5, choices=GENDER)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    class Meta:
        ordering = ['first_name']
        unique_together = (
            "first_name",
            "last_name",
            "date_of_birth",
            "phone_number"
        )

    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Student, self).save(*args, **kwargs)
