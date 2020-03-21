from django.urls import path
from django.contrib.auth import views as auth_views
from ticket_system.ticket import views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
    path('tasks/<int:task_id>/edit/', views.task_edit, name='task-edit'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    ]
