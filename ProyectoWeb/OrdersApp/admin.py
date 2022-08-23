from django.contrib import admin
from .models import Order, OrderLine

#Admin Panel Tablas del Modelo:
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'created_at')
    list_filter = ['created_at']
    readonly_fields = ['created_at']

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'product_id', 'quantity', 'created_at')
    list_filter = ['order_id', 'user_id', 'product_id', 'created_at']
    search_fields = ('order_id', 'user_id', 'product_id', 'created_at')
    readonly_fields = ['created_at']

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)