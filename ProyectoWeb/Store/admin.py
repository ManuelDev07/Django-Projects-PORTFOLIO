from django.contrib import admin
from .models import CategoryProduct, Product

#Admin Panel Tablas del Modelo:
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'price', 'categories', 'sold', 'created_at') #Columnas de la tabla
    list_filter = ['categories', 'sold', 'created_at'] #Filtros
    search_fields = ['name', 'price', 'categories'] #Casilla de Búsqueda
    readonly_fields = ['created_at'] #Para leer los datetimeFields

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at') #Columnas de la tabla
    list_filter = ['name', 'created_at', 'updated_at'] #Filtros
    search_fields = ['name'] #Casilla de Búsqueda
    readonly_fields = ['created_at', 'updated_at'] #Para leer los datetimeFields

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)