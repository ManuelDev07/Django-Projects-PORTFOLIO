from django.shortcuts import redirect
from ShoppingCartApp.shopping_cart import Shopping_Cart_Class #Se importa la clase del carrito
from Store.models import Product #Se importan el modelo de los productos para poder acceder a los datos de cada item
from django.contrib import messages

# Create your views here.
def add_product_cart(request, product_id):#Función que AGREGARÁ los productos mediante llamadas a la clase
    #Creo el carrito instanciando la clase creada:
    cart = Shopping_Cart_Class(request)
    
    #obtengo el producto que se agregará al carrito mediante su id:
    product = Product.objects.get(id=product_id)

    #Una vez teniendo el producto y el carrito solo queda agregarlo:
    cart.add_product(product=product) #agrego mediante la llamada al método

    return redirect('tienda') 

def del_product_cart(request, product_id): #Función que ELIMINARÁ los productos mediante llamadas a la clase
    cart = Shopping_Cart_Class(request)
    del_prod = Product.objects.get(id=product_id)
    cart.delete_product(del_prod) #elimino mediante la llamada al método

    return redirect('tienda')

def discount_product_cart(request, product_id):#Función que RESTARÁ los productos mediante llamadas a la clase
    cart = Shopping_Cart_Class(request)
    disc_prod = Product.objects.get(id=product_id)
    cart.discount_product(disc_prod) #resto mediante la llamada al método

    return redirect('tienda')

def clean_cart(request):#Función que LIMPIARÁ el carrito mediante llamadas a la clase
    cart = Shopping_Cart_Class(request)
    cart.clean_shopping_cart() #limpio mediante la llamada al método

    return redirect('tienda')