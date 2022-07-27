from django.shortcuts import render, HttpResponse
from ShoppingCartApp.shopping_cart import Shopping_Cart_Class

# Create your views here.
def home(request):#Página Principal

    cart = Shopping_Cart_Class(request)#Inicio el carrito de compras para evitar errores(esto es opcional por si se presentan errores al cargar la página)

    return render(request, 'home.html', {'cart':cart})