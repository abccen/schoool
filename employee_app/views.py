from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from employee_app.models import Department, Position, Employee
from employee_app.serializers import DepartmentSerializer, \
    PositionSerializer, EmployeeSerializer
from rest_framework import viewsets
"""
CRUD
C = create
R = retrive
U = update
D = destroy
"""


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Department.objects.all().order_by('-id')
    serializer_class = DepartmentSerializer


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Position.objects.all().order_by('-id')
    serializer_class = PositionSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    lookup_field = 'pk'
    ordering_fields = ['user']
    search_fields = ['user__username']
    filterset_fields = ['position']
