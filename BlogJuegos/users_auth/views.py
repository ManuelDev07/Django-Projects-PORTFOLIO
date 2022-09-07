from django.shortcuts import render, redirect
from django.contrib import messages
from users_auth.forms import Register_Form
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register_user(request):
    """Vista que permitirá a los usuarios crearse una cuenta en la tienda.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá un renderizado del formulario de registro de usuarios.
    """

    if request.method == 'POST':
        form = Register_Form(request.POST) #obtengo los datos para el form

        if form.is_valid(): #verifico que los datos enviados por la request sean válidos
            new_user = form.save() #si es True se guarda el nuevo usuario en la BBDD

            #mensaje flash de feedback:
            messages.success(request, f'Te haz Registrado! Bienvenid@ {new_user.username}')

            login(request, new_user) #dejo al usuario logeado

            return redirect('all_posts')
        else:
            messages.success(request, 'Ha Ocurrido un error, ingresa tus datos correctamente para registrarte.')

    else:
        form = Register_Form()#form vacío

    return render(request, 'users_auth_templates/register.html', {'form':form})

def login_user(request):
    """Vista que permitirá a los usuarios iniciar sesión en el blog.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá un renderizado del formulario de login.
    """

    if request.method == 'POST':
        #se obtienen los datos del input del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password) #se autentican

        if user is not None: #si el usuario está en la bbdd se dará acceso
            login(request, user)
            return redirect('all_posts')
        else: #caso contrario se da un mensaje feedback
            messages.error(request, 'Datos Incorrectos...')
    
    return render(request, 'users_auth_templates/login.html')

def logout_user(request):
    """Función que cerrará la sesión del usuario actual.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        redirect: devolverá una redirección al formulario de inicio de sesión.
    """
    logout(request)

    return redirect('login_user')