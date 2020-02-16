from django.urls import path

from ticket_system.ticket import views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task-detail'),
    ]
