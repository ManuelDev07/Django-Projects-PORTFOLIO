from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #Store App:
    path('home/', include('Store.urls')),

    #Search App:
    path('', include('Search.urls')),

    #Shopping Cart App:
    path('cart/', include('ShoppingCart.urls')),

    #AuthUser App:
    path('users/', include('AuthUsers.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)