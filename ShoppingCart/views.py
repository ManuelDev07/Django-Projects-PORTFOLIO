from django.shortcuts import redirect, render
from ShoppingCart.shopping_cart import Shopping_Cart_Class #Se importa la clase del carrito
from Store.models import Manga #Se importan el modelo de los Mangatos para poder acceder a los datos de cada item
from django.contrib import messages

# Create your views here.
def add_product_cart_store(request, id):
    """Función que AGREGARÁ los productos mediante llamadas a la clase desde la página principal de la tienda.

    Args:
        request (HTTP): Petición HTTP
        id (int): identificador del producto a agregar

    Returns:
        redirect: redireccionará a la misma página principal para que el usuario siga navegando por la tienda.
    """
    #Creo el carrito instanciando la clase creada:
    cart = Shopping_Cart_Class(request)
    
    #obtengo el producto que se agregará al carrito mediante su id:
    product = Manga.objects.get(id=id)

    #Una vez teniendo el producto y el carrito solo queda agregarlo:
    cart.add_product(product=product) #agrego mediante la llamada al método

    messages.success(request, 'Agregado con Éxito!')

    return redirect('inicio')

def add_product_cart_page(request, id):
    """Función que AGREGARÁ los productos mediante llamadas a la clase dentro de la misma página del carrito sin redireccionar.

    Args:
        request (HTTP): Petición HTTP
        id (int): identificador del producto a agregar

    Returns:
        render: devolverá el renderizado de la página del carrito para que el usuario siga administrando su carrito.
    """
    
    #Creo el carrito instanciando la clase creada:
    cart = Shopping_Cart_Class(request)
    
    #obtengo el producto que se agregará al carrito mediante su id:
    product = Manga.objects.get(id=id)

    #Una vez teniendo el producto y el carrito solo queda agregarlo:
    cart.add_product(product=product) #agrego mediante la llamada al método

    return render(request, 'my_cart.html')

def del_product_cart(request, id):
    """Función que ELIMINARÁ los productos mediante llamadas a la clase.

    Args:
        request (HTTP): Petición HTTP
        id (int): identificador del producto a agregar

    Returns:
        render: devolverá el renderizado de la página del carrito para que el usuario siga administrando su carrito.
    """ 
    cart = Shopping_Cart_Class(request)
    del_prod = Manga.objects.get(id=id)
    cart.delete_product(del_prod) #elimino mediante la llamada al método

    return render(request, 'my_cart.html')

def discount_product_cart(request, id):
    """Función que RESTARÁ los productos mediante llamadas a la clase.

    Args:
        request (HTTP): Petición HTTP
        id (int): identificador del producto a agregar

    Returns:
        render: devolverá el renderizado de la página del carrito para que el usuario siga administrando su carrito.
    """     
    cart = Shopping_Cart_Class(request)
    disc_prod = Manga.objects.get(id=id)
    cart.discount_product(disc_prod) #resto mediante la llamada al método

    return render(request, 'my_cart.html')

def show_cart(request):
    """Vista para la página del carrito.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página del carrito.
    """       
    cart = Shopping_Cart_Class(request)

    return render(request, 'my_cart.html')

def clean_cart(request):
    """Función que LIMPIARÁ el carrito mediante llamadas a la clase.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página del carrito vacío.
    """     
    cart = Shopping_Cart_Class(request)
    cart.clean_shopping_cart() #limpio mediante la llamada al método

    return render(request, 'my_cart.html')