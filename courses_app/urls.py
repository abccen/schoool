from django.urls import path
from courses_app.views import CourseViewSet

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list'}), name='course-list'),
]
