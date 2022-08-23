from django.urls import path
from ShoppingCartApp import views

#app_name = 'cart'

urlpatterns = [
    path('add_product/<int:product_id>/', views.add_product_cart, name='agregar-prod'),
    path('delete_product/<int:product_id>/', views.del_product_cart, name='eliminar-prod'),
    path('discount_product/<int:product_id>/', views.discount_product_cart, name='restar-prod'),
    path('clean_cart/', views.clean_cart, name='limpiar_carrito'),
]