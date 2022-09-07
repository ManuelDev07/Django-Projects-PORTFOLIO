from django.contrib import admin
from .models import Genres_Model, Category_Model, Console_Model, Posts_Model, Comments_Model

#Visualización del Admin Panel:
class Genres_Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class Category_Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class Console_Admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class Posts_Admin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['name', 'created_at']
    readonly_fields = ['created_at']
    list_filter = ['created_at']

class Comments_Admin(admin.ModelAdmin):
    list_display = ['comment', 'commented_on', 'commented_by']

# Register your models here.
admin.site.register(Genres_Model,Genres_Admin)
admin.site.register(Category_Model, Category_Admin)
admin.site.register(Console_Model, Console_Admin)
admin.site.register(Posts_Model, Posts_Admin)
admin.site.register(Comments_Model, Comments_Admin)

#Títulos del Admin Panel:
admin.site.site_header = 'Blog Juegos'
admin.site.index_title = 'Admin BlogJuegos'
admin.site.site_title = 'Login Admin Panel'