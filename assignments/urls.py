from django.urls import path
from .views import AssignmentViewSet

assignment_list = AssignmentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

assignment_detail = AssignmentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path('', assignment_list, name='assignment-list'),
    path('<int:pk>/', assignment_detail, name='assignment-detail'),
]