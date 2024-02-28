from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:pk>/', views.taskDetail, name='task-detail'),
    path('addTask/',views.addTask, name='add-task'),
    path('editTask/<int:pk>/',views.updateTask, name='edit-task'),
    path('deleteTask/<int:pk>/',views.deleteTask, name='delete-task'),
    path('taskComplete/<int:pk>/',views.completeTask, name='task-complete'),
    path('taskPending/<int:pk>/',views.pendingTask, name='task-pending'),

]