from cmath import log
from django.shortcuts import redirect, render
from AuthUsersApp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def register_users(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            login(request, new_user)

            messages.success(request, "Te haz Registrado Correctamente!!")

    return render(request, 'register.html', {'form':form})

def login_users(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Bienvenido de vuelta ")
            
            return redirect('ingresar')

        else:
            messages.error(request, "ERROR! Datos incorrectos...")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)

    return redirect('ingresar')