from django.urls import path, include
from AuthUsers import views

urlpatterns = [
    path('register/', views.register_user, name='registrar'),
    path('login/', views.login_user, name='ingresar'),
    path('logout/', views.logout_user, name='cerrar-sesion')
]
