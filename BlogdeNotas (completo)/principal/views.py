from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from principal.forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from principal.models import Note


# Create your views here.
def inicio(request):
    return render(request, "inicio.html", {
        'title':'Inicio'
    })

def aboutMe(request):
    return render(request, 'about.html', {
        'title':"Sobre Mí"
    })

def register(request):
    create = RegisterForm()

    if request.method == 'POST':
        create = RegisterForm(request.POST)
        
        if create.is_valid():
            create.save()
            messages.success(request, "Te haz registrado correctamente!")

            return redirect('inicio')
        else :
            messages.success(request, "Intenta de nuevo")

    return render(request, "register.html", {
        'title':'Registrarme',
        'create':create,
    })

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect("inicio")
        else:
            messages.warning(request, 'Los datos ingresados no son correctos...')

    return render(request, 'login.html', {
        'title':"Ingresar"
    })


def logout_user(request):

    logout(request)

    return redirect('ingresar')


@login_required(login_url='ingresar')
def createNote(request):
    return render(request,'create.html')

@login_required(login_url='ingresar')
def saveNote(request):
    if request.method == 'POST':

        newTitle = request.POST['title']
        newAuthor = request.POST['author']
        newContent = request.POST['content']

        if len(newTitle) <=3:
            return HttpResponse("Título Muy Corto...")

        newNote = Note(
            title = newTitle,
            author = newAuthor,
            content = newContent,
        )

        newNote.save()
        messages.success(request, f"Se ha guardado la nota: {newNote.title} ")

    return redirect('listar-notas')


@login_required(login_url='ingresar')
def showNote(request):
    list = Note.objects.all()

    return render(request, 'show.html', {
        'title':'Todas Mis Notas',
        'list':list
    })


@login_required(login_url='ingresar')
def deleteNote(request, id):
    eliminarNota = Note.objects.get(pk = id)
    eliminarNota.delete()
    return redirect('listar-notas')

