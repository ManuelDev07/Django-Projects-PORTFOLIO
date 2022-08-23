from django.shortcuts import render, redirect
from ListApp.models import To_Do_Model 
from django.contrib import messages

# Create your views here.
def create_tasks(request): #Página para el formulario para crear tareas
    """View que será el formulario para la creación de nuevas Tareas.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render, redirect: Devolverá la redirección para ver la nueva tarea creada o un render con un mensaje de error
    """

    #Verifico la petición y almaceno en una variable los datos de los inputs:
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']

        #Mensaje de error:
        if len(title) <= 3: 
            messages.error(request,'ERROR! Título Muy Corto.')
            return render(request, 'create.html')

        else:
            #Conservo los datos y los guardo:
            new_task = To_Do_Model(
                title = title,
                desc = desc
            )
            
            new_task.save() #Guardo la nueva tarea
            
            return redirect('mis_tareas') #Devuelvo a la página principal

    return render(request, 'create.html')

def remove_task(request, id:int): #Botón para borrar tareas
    """View que eliminará las tareas pendientes.

    Args:
        request (HTTP): Petición HTTP.
        id (int): primary key de la tarea.

    Returns:
        redirect: redireccionará a la página principal de tareas pendientes
    """
    #query
    task = To_Do_Model.objects.get(id=id)

    task.removed_or_not = True #modifico el campo bool a True
    task.save() #guardo los datos

    return redirect('mis_tareas') #Devuelvo a la página principal 

def complete_task(request, id:int): #Botón para completar tareas
    """View que marcará como completadas las tareas pendientes.

    Args:
        request (HTTP): Petición HTTP.
        id (int): primary key de la tarea.

    Returns:
        redirect: redireccionará a la página principal de tareas pendientes
    """
    #query
    task = To_Do_Model.objects.get(id=id)

    task.done = True #modifico el campo bool a True
    task.save() #guardo los datos

    return redirect('mis_tareas') #Devuelvo a la página principal 

def perma_remove_task(request, id:int): #Botón para borrar tareas permanentemente
    """View que eliminará por completo de la BBDD las tareas que hayan sido terminadas o eliminadas.

    Args:
        request (HTTP): Petición HTTP.
        id (int): primary key de la tarea.

    Returns:
        redirect: redireccionará a la página principal de tareas pendientes
    """
    #query
    task = To_Do_Model.objects.get(id=id)

    task.delete() #elimino el objeto de la BBDD

    return redirect('tareas_eliminadas') #Devuelvo a la página principal 
