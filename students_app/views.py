from rest_framework import viewsets
from students_app.models import Student
from students_app.serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
