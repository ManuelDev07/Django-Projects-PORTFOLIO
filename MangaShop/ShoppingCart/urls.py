from django.urls import path
from ShoppingCart import views

urlpatterns = [
    path('add/<int:id>/', views.add_product_cart_store, name='agregar'),
    path('add-in-page/<int:id>/', views.add_product_cart_page, name='agregar_en_pagina'),
    path('delete/<int:id>/', views.del_product_cart, name='eliminar'),
    path('discount/<int:id>/', views.discount_product_cart, name='restar'),
    path('clean_cart/', views.clean_cart, name='limpiar_carrito'),
    path('my-cart/', views.show_cart, name='carrito')
]