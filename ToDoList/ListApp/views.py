from django.shortcuts import render
from .models import To_Do_Model

# Create your views here.
def all_tasks(request): #Página para Mostrar Todas las Tareas
    """View que se encargará solo de mostrar las tareas que NO han sido ni eliminadas ni completadas.

    Args:
        request (HTTP): Petición HTTP.

    Returns:
        render: renderizará al html para mostrar el query solicitado.
    """
    #Query:
    tasks = To_Do_Model.objects.filter(done=False, removed_or_not=False)

    return render(request, 'all_tasks.html', {'tasks':tasks})

def removed_tasks(request):#Página para Mostrar Todas las Tareas Eliminadas
    """View que se encargará solo de mostrar las tareas que han sido eliminadas.

    Args:
        request (HTTP): Petición HTTP.

    Returns:
        render: renderizará al html para mostrar el query solicitado.
    """
    #Query:
    tasks = To_Do_Model.objects.filter(done=False, removed_or_not=True)

    return render(request, 'removed_tasks.html', {'tasks':tasks})

def completed_tasks(request): #Página para Mostrar Todas las Tareas Completadas
    """View que se encargará solo de mostrar las tareas que han sido completadas.

    Args:
        request (HTTP): Petición HTTP.

    Returns:
        render: renderizará al html para mostrar el query solicitado.
    """
    #query:
    tasks = To_Do_Model.objects.filter(done=True, removed_or_not=False)

    return render(request, 'completed_tasks.html', {'tasks':tasks})
