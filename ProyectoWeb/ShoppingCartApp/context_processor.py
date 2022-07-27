#En este archivo se trabajará como un 'context processor' que permitirá crear una variable global que almacenará y sumará el precio 
#total de los productos que se vayan agregando al carrito y será accesible a través de toda la página.
from .shopping_cart import Shopping_Cart_Class

def total_price(request):
    total = 0 #creo la variable global

    #Verifico si el usuario está autenticado:
    if request.user.is_authenticated:
        #Recorro los elementos del dict del carrito con el par key:value
        for key, value in request.session['cart'].items():
            total = (float(value['price'])) + total
    

    return {'total_price':total}

#Para que el context_processor sea accesible desde cualquier lugar del proyecto debo registrar la ruta de este archivo en settings.py