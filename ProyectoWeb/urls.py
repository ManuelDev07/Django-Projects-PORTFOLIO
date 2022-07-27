"""ProyectoWeb URL Configuration

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
from django.urls import path, include

#Estos dos es para usar las URL de las imagenes y poder verlas al acceder a estas desde el Admin Panel
from django.conf import settings
from django.conf.urls.static import static

#Mis URL:
urlpatterns = [
    path('admin/', admin.site.urls),

    #Llamo las URL de WebApp:
    path('', include('WebApp.urls')),

    #Llamo las URL de Services:
    path('', include('Services.urls')),

    #Llamo las URL de Blog:
    path('blog/', include('Blog.urls')), #En este caso agregue URL ya que dentro de 'Blog' me redirigirá a otras URL dentro de la app 

    #Llamo las URL de Contact:
    path('', include('Contact.urls')),

    #Llamo las URL de Store:
    path('store/', include('Store.urls')), #Aquí se volverá a redirigir a otras URL dentro de la app 'Store'

    #Llamo las URL de ShoppingCartApp:
    path('cart/', include('ShoppingCartApp.urls')), #Aquí se volverá a redirigir a otras URL dentro de la app 'ShoppingCartApp'

    #Llamo las URL de AuthenticationUsersApp:
    path('user/', include('AuthenticationUsersApp.urls')), 

    #Llamo las URL de OrderApp:
    path('order/', include('OrdersApp.urls')),
]

#Agrego las URL para las imágenes:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)