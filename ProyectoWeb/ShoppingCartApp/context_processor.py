#En este archivo se trabajará como un 'context processor' que permitirá crear una variable global que almacenará y sumará el precio 
#total de los productos que se vayan agregando al carrito y será accesible a través de toda la página.
from .shopping_cart import Shopping_Cart_Class

def total_price(request):
    """Función que creará una variable global (context_procressor) para poder
    visualizar el precio total a pagar del carrito de compras.

    Args:
        request (HTTP): petición HTTP

    Returns:
        dict: devolverá el diccionario con el valor total del precio.
    """
    total = 0 #creo la variable global

    #Verifico si el usuario está autenticado:
    if request.user.is_authenticated:
        #Recorro los elementos del dict del carrito con el par key:value solo si es carro existe en la sesión
        if 'cart' in request.session:
            for key, value in request.session['cart'].items():
                total += (float(value['price']))
    
    return {'total_price':total}

#Para que el context_processor sea accesible desde cualquier lugar del proyecto debo registrar la ruta de este archivo en settings.py