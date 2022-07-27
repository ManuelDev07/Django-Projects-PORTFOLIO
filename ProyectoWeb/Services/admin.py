from django.contrib import admin
from .models import Services

#Admin Panel Tablas del Modelo:
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at') #Orden Visual
    search_fields = ('title', 'created_at', 'updated_at') #Casilla de Búsqueda
    list_filter = ['created_at', 'updated_at', 'title'] #Filtros 
    readonly_fields = ('created_at', 'updated_at') #Para que los campos al ser datetimefield se vean en el panel de admin

# Register your models here.
admin.site.register(Services, ServicesAdmin)