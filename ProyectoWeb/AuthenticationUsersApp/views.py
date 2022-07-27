from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #Para crear el formulario de creación y login de usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register_user(request): #Página para registrar usuarios
    #instancio la clase del form de usuarios:
    user_form = UserCreationForm()

    #Verifico si los datos han sido recibidos:
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST) #Guardo la data
        #Verifico si los datos que ha ingresado el usuario son válidos:
        if user_form.is_valid():
            user = user_form.save() #creo el usuario
            #Se le informa al usuario que se ha creado su usuario en la página
            
            login(request, user) #De una vez queda logeado el usuario

            messages.success(request, 'Te haz registrado correctamente! 🥳')
            
            return redirect('inicio')

        else:#Por si el usuario ha cometido un error al ingresar sus datos se muestra un mensaje flash
            messages.error(request, 'ERROR! Intentalo de nuevo...')

            return redirect('registrar_usuario')

    return render(request, 'register.html', {'user_form':user_form})

def login_user(request): #Página para logear usuarios
    #Verifico si he recibido los datos con POST:
    if request.method == 'POST':
        #recibo los datos del formulario de login:
        username = request.POST.get('username')
        passwrd = request.POST.get('passwrd')

        #lo autentico:
        user = authenticate(request, username=username, password=passwrd)

        #Verifico si el usuario existe (si ya está registrado en la página):
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido de vuelta! ')

            return redirect('inicio')
        
        else: #Caso contrario informo con un mensaje flash por si el usuario ingreso datos incorrectos:
            messages.error(request, 'Datos Incorrectos 🤨')

    return render(request, 'login.html')

def logout_user(request): #Función para cerrar sesión

    logout(request)

    return redirect('login')