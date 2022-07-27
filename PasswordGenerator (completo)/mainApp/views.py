from django.shortcuts import render
from django.contrib import messages
import string
from random import shuffle, choice

# Create your views here.
def index(request): #Página Principal
    """Vista principal de la página.

    Args:
        request: request HTTP

    Returns:
        render: renderizado de la página
    """
    return render(request, 'index.html')

def show_password(request): #Crear y Mostrar Contraseña
    """Función que se encargará de crear la contraseña con el largo que fué enviado a través del request.

    Args:
        request: request HTTP

    Returns:
        render: renderizado de la página con el string que se creó.
    """
    alf = string.ascii_letters #Letras tanto minúsculas como Mayúsculas
    numc = string.digits #Números
    spc = "!@#$%^&*()" #Caractéres especiales

    chars = list(alf + numc + spc) #Los junto todos en un string
    shuffle(chars) #Los desordeno

    #Verifico si el usuario ha ingresado algún valor en el input
    if request.GET['long']:
        if request.method == 'GET': #verifico la request
            new_passwrd= [] #Lista nueva que contendrá cada caracter de la contraseña

            leng = request.GET['long'] #Guardo en una variable el valor que se ha enviado en el input(el cual será el largo de la contraseña)
            
            if int(leng) > 60:
                messages.error(request,'ERROR! Es muy largo')
                
                return render(request, 'index.html')

            elif int(leng) < 1:
                messages.error(request,'ERROR! Es muy corto')
                
                return render(request, 'index.html')

            else:
                for i in range(int(leng)):
                    char = choice(chars) #Se selecciona un valor al azar del string
                    new_passwrd.append(char) #Se agrega a la lista

                shuffle(new_passwrd)#Los desordeno
                password = ''.join(new_passwrd) #junto todos los elementos de la lista para convertirlos en cadena

                return render(request, 'index.html', {'password':password})
                    
    else: #Caso contrario en caso de que el usuario haya dejado vacío el input
        messages.error(request, 'ERROR! Debes establecer un largo para tu nueva contraseña...')

        return render(request, 'index.html')