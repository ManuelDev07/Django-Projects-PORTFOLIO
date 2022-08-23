from django.urls import path
from ConfListApp import views

urlpatterns = [
    path('create/', views.create_tasks, name='crear'),
    path('complete/<int:id>/', views.complete_task, name='completar'),
    
    #Borrar:
    path('delete/<int:id>/', views.remove_task, name='eliminar'), #Borrar
    path('perma-delete/<int:id>/', views.perma_remove_task, name='perma_eliminar'), #Borrar de la BBDD
]
