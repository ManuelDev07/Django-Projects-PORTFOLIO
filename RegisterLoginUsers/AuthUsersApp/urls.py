from django.urls import path
from AuthUsersApp import views

urlpatterns = [
    path('register/', views.register_users, name='registrar'),
    path('login/', views.login_users, name='ingresar'),
    path('logout/', views.logout_user, name='salir')
]