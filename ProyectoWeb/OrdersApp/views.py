from django.shortcuts import render, redirect
from OrdersApp.models import OrderLine, Order
from django.contrib.auth.decorators import login_required #Para los decoradores
from ShoppingCartApp.shopping_cart import Shopping_Cart_Class #Para acceder al carrito
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags #Para eliminar el contenido HTML del mesanje a que se enviará
from django.core.mail import send_mail #Para enviar mail

# Create your views here.
@login_required(login_url='/user/login')
def order_admint(request):
    #Instancio la clase y creo el pedido que el usuario está haciendo
    order = Order.objects.create(user=request.user)

    #Creo el carrito para poder acceder a los datos de esos productos que están dentro:
    cart = Shopping_Cart_Class(request)
    
    order_list = list() #Donde se guardarán los productos

    #Recorro el carrito y lo agrego a la lista de pedidos
    for key, value in cart.cart.items():
        #Agrego a la lista mediante la clase OrderLine con los datos del producto (como su id, cantidad que hay en el carrito, el id del user, etc)
        order_list.append(OrderLine(
            user = request.user,
            product_id = key,
            quantity = value['quantity'],
            order = order #el pedido creado anteriormente
        ))
    
    #Luego los elementos de la lista los tengo que ingresar a la linea de pedidos (al modelo BBDD OrderLine) 
    #Mediante bulk_create() el cual sirve como si fueran varios INSERT INTO en SQL
    OrderLine.objects.bulk_create(order_list)

    #Le informo al usuario que el pedido se ha procesado correctamente:
    messages.success(request, 'Pedido Realizado con Éxito!')
    
    #Llamada a una función que enviará al correo un mensaje al usuario con los detalles del pedido como parámetros:
    order_email(order=order, order_list=order_list, username=request.user.username, email_user=request.user.email)

    return redirect('tienda')

def order_email(**kwargs): #el kwargs es para pasar varios argumentos
    subject = 'Gracias por tu Compra! :D'#Asunto
    #Mensaje/Cuerpo del email:
    message = render_to_string('orderEmails/order.html', { #Se usará ya que el mensaje se creará mediante un archivo.html
        #Se acceden a los parámetros mediante kwargs.get('nombreParámetros')
        'username':kwargs.get('username'),
        'order':kwargs.get('order'),
        'order_list':kwargs.get('order_list'),
    })

    #Este será el mensaje que recibirá la persona:
    message_text = strip_tags(message) #se quita las tags HTML del mensaje
    from_email = 'manudesarrolla07@gmail.com' #Emisor (dueño de la tienda)
    to = kwargs.get('email_user') #Receptor (email del usuario)


    #Se envía el correo:
    send_mail(subject, message_text,from_email, [to], html_message=message)