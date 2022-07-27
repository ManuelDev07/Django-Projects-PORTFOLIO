from django.urls import path
from AuthenticationUsersApp import views

urlpatterns = [
    path('register/', views.register_user, name='registrar_usuario'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]