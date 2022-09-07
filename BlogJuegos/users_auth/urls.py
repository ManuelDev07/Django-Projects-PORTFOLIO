from users_auth import views
from django.urls import path

urlpatterns = [
    path('registrar/', views.register_user, name='register_user'),
    path('iniciar-sesion/', views.login_user, name='login_user'),
    path('cerrar-sesion/', views.logout_user, name='logout_user')
]
