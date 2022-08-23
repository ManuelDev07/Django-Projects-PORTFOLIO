from django.contrib import admin
from .models import Articles, Clients, Orders

#Cada una de estas clases es para ver la tabla en Admin Panel:
class ClientsAdmin(admin.ModelAdmin): 
    list_display = ('name', 'address', 'email', 'phone_number') #Para ver con cada una de sus columnas del modelo y mas organizada
    search_fields = ('name', 'email') #Para crear una CASILLA DE BÚSQUEDA, de esta manera buscaria por nombre y el email (puedo agregar mas campos)

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'price')
    list_filter = ['section'] #Para buscar mediante un FILTRO los articulos de x categoria 

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'received')
    list_filter = ['date', 'received']

# Register your models here.
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Orders, OrdersAdmin)