from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    #Llamo las URL de AuthUsersApp:
    path('', include('AuthUsersApp.urls'))
]

urlpatterns += static(settings.MEDIA_URL, documet_root=settings.MEDIA_ROOT)