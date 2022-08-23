from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #MainApp:
    path('to-do/', include('ListApp.urls')),

    #ConfigureApp:
    path('', include('ConfListApp.urls'))
]
