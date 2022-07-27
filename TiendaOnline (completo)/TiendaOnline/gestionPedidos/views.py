from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from gestionPedidos.models import Articles
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def search_articles(request): #Página para buscar articulos
    return render(request, 'search_articles.html')

def search(request): #Página para mostrar los articulos buscados (si los hay)
    #El if es para verificar que el usuario NO ha introducido una cadena de caracteres vacía
    if request.GET['article']:

        #Se empieza a buscar el articulo en la BBDD:
        article = request.GET['article'] #guardo en una variable lo que ha buscado la persona 
        if len(article) > 41:
            messages.error(request, 'El texto que haz ingresado es muy largo. Intenta de nuevo...') #Mensaje por si el nombre del articulo es mas largo de lo debido.

            return render(request, 'search_articles.html')
        
        else:
            articles = Articles.objects.filter(name__icontains = article)#Se filtra/busca el nombre del campo a buscar con __icontains = variable. El icontains es lo mismo que usar LIKE de SQL

        return render(request, 'results_searchs.html', {
            'articles':articles,
            'query':article.title()
        })

    else:
        messages.error(request, 'Búsqueda Vacía...') #Mensaje por si se ha dejado la casilla de búsqueda vacía.

        return render(request, 'search_articles.html')
        
def contact(request): #Página de Contacto
    if request.method == 'POST':

        #Envio de Emails:
        #Guardo los datos del formulario en variables:
        subject = request.POST['subject'] 
        from_email = settings.EMAIL_HOST_USER
        message = request.POST['message'] + ' ' + request.POST['email']
        recipient_list = ['manudesarrolla07@gmail.com'] #Dirección donde quiero que lleguen los mensjaes del form
        
        #Se envia todos los datos del form al email:
        send_mail(subject, message, from_email, recipient_list)

        #Mensaje al ser enviado el mail:
        messages.success(request, 'Mensaje Enviado!') 
        

    return render(request, 'contact.html')