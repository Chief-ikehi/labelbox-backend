from django.urls import path
from .views import ProjectListCreateView, TaskListCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]
