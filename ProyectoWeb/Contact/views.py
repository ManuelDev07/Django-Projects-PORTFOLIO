from django.shortcuts import render, redirect
from django.contrib import messages #Mensajes Flash
from Contact.forms import ContactForm #Formulario del Contacto

#Envio de emails
from django.core.mail import send_mail, EmailMessage
from django.conf import settings


# Create your views here.
def contact(request): #Página de Contacto
    #Envío de Emails:
    #Instancio la clase del formulario:
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)#vuelvo a definir la variable pero con los datos obtenidos en la request

        if contact_form.is_valid(): #En caso del formulario esté todo correcto
            #Se guardan los datos de cada campo:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')

            #Formo el mensaje con los datos recibidos:
            email_message = EmailMessage(
                'Mensaje desde APP Django', #Asunto
                f'El Usuario {name} <({email})>. Te ha enviado un mensaje: {subject}', #Cuerpo del mensaje enviado
                '', #correo del remitente
                ['manudesarrolla07@gmail.com'], #Correo del receptor
                reply_to=[email] #Responder al correo del remitente
            )

            #Y se envia:
            try:
                email_message.send()
                
                #Mensaje flash al ser enviado el mail:
                messages.success(request, 'Correo Enviado! 🥳')

                #return redirect('contacto') #Me redirecciona a la misma página contacto
                return redirect('/contact/?OK') 

            except:
                #Mensaje flash al NO enviarse el mail:
                messages.error(request, 'No se ha podido enviar tu correo... 😔💔')

                return redirect('/contact/?ERROR')

    return render(request, 'contact.html', {'form':contact_form})