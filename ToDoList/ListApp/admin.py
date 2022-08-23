from django.contrib import admin
from .models import To_Do_Model

#Admin Panel Visualization:
class To_Do_Admin(admin.ModelAdmin):
    list_display = ['title', 'removed_or_not','done','created_at']
    list_filter = ['done', 'removed_or_not','created_at']
    search_fields = ['title']

# Register your models here.
admin.site.register(To_Do_Model,To_Do_Admin)

#Page Title Admin Panel:
admin.site.site_header = 'ToDo Admin'
admin.site.index_title = 'Configuración de las Tareas'