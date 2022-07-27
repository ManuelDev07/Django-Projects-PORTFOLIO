"""BlogdeNotas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from principal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.inicio, name="404"),
    path("inicio/", views.inicio, name="inicio"),
    path('sobre-mi/', views.aboutMe, name="sobre-mi"),
    path('registrar/', views.register, name="registrar"),
    path('ingresar/', views.login_user, name="ingresar"),
    path("cerrar/", views.logout_user, name="salir"),
    path("listar/", views.showNote, name="listar-notas"),
    path("crear/", views.createNote, name="crear-nota"),
    path("save/", views.saveNote, name="save-nota"),
    path("delete/<int:id>", views.deleteNote, name="borrar-nota"),
]

admin.site.site_header = "Blog de Notas"
admin.site.site_title = "Datos"
admin.site.index_title = "Panel para Gestionar Usuarios"