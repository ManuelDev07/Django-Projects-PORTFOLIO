from django.urls import path
from OrdersApp import views

urlpatterns = [
    path('', views.order_admint, name='administrar_pedido')
]