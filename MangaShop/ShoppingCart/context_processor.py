#variable global para el precio:

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