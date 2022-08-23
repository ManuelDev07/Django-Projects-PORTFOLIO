from django.contrib import admin
from .models import Genre, Manga, Author, Demography

# Visualization Models Admin Panel
class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre', 'available']
    list_filter = ['genre', 'available']
    search_fields = ['genre']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class DemograpyAdmin(admin.ModelAdmin):
    list_display = ['demography', 'available']
    list_filter = ['demography', 'available']
    search_fields = ['demography']

class MangaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'author', 'year', 'state', 'country', 'recommended_age', 'available']
    search_fields = ['name', 'author']
    list_filter = ['author','available', 'year', 'state', 'country', 'recommended_age']

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Demography, DemograpyAdmin)
admin.site.register(Manga, MangaAdmin)

#Titles Admin Panel: 
admin.site.site_title = 'Configuración Tienda Manga'
admin.site.site_header = 'Admin Tienda Manga'