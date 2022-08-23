from django.shortcuts import render, redirect
from AuthUsers.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register_user(request):
    """Vista que permitirá a los usuarios crearse una cuenta en la tienda.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá un renderizado del formulario de registro de usuarios.
    """
    form = RegisterForm()#instancio el formulario personalizado de registro

    if request.method == 'POST':
        form = RegisterForm(request.POST) #obtengo los datos para el form

        if form.is_valid(): #verifico que los datos enviados por la request sean válidos
            new_user = form.save() #si es True se guarda el nuevo usuario en la BBDD

            #mensaje flash de feedback:
            messages.success(request, f'Te haz Registrado! Bienvenid@ {new_user.username}')

            login(request, new_user) #dejo al usuario logeado

            return redirect('inicio')

        else:
            messages.success(request, 'Ha Ocurrido un error, ingresa tus datos correctamente para registrarte.')

    return render(request, 'register.html', {'form':form})

def login_user(request):
    """Vista que permitirá a los usuarios poder iniciar sesión con sus cuentas en la tienda.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá un renderizado del formulario de login.
    """    
    
    if request.method == 'POST': #obtengo los datos ingresados del form mediante la request
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) #autentico esos datos obtenidos en mi BBDD

        if user is not None: #Si el usuario existe ingresará
            login(request, user)
            messages.success(request, f'Bienvenid@ de nuevo!! {username.upper()} 🥳')

            return redirect('inicio')

        else: #Caso contrario se muestra un mensaje
            messages.error(request, 'Datos Incorrectos...')

    return render(request, 'login.html')

def logout_user(request):
    """Función que tendrá como objetivo cerrar la sesión de un usuario.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        redirect: redireccionará a la página de logeo.
    """
    logout(request)

    return redirect('ingresar')