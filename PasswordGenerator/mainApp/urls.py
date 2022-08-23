from django.urls import path, include
from mainApp import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('show-password/', views.show_password, name='generador_contraseña')
]
