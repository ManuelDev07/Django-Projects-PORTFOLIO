from django.contrib import admin
from .models import Categories, Posts

#Admin Panel Tablas del Modelo:
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')
    list_filter = ['name', 'created_at']
    readonly_fields = ('created_at', 'updated_at')

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','created_at', 'updated_at')#Los campos que son ManyToManyFields no se pueden mostrar en list_display
    list_filter = ['author', 'category', 'created_at', 'updated_at']
    search_fields = ('title', 'author', 'category')
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Posts, PostsAdmin)