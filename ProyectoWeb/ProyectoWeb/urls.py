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