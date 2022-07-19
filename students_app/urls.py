from django.urls import path
from students_app.views import StudentViewSet

urlpatterns = [
    path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student-list'),
    path('<int:pk>/', StudentViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update'
        }
    ),
         name='student-detail'
         ),
]
