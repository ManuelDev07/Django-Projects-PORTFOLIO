from django.urls import path
from ListApp import views

urlpatterns = [
    path('mis-tareas/', views.all_tasks, name='mis_tareas'),
    path('tareas-eliminadas/', views.removed_tasks, name='tareas_eliminadas'),
    path('tareas-completadas/', views.completed_tasks, name='tareas_completadas')
]
