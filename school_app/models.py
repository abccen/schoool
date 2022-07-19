from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name
