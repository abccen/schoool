from rest_framework.validators import UniqueTogetherValidator

from students_app.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_number', 'email', 'gender', 'course']
        validators = [
            UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=['first_name', 'last_name', 'date_of_birth', 'phone_number']
            )
        ]
