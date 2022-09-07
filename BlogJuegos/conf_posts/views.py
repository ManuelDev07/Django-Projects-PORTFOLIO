from django.shortcuts import render, redirect
from conf_posts.forms import Create_Post
from django.contrib import messages
from django.contrib.auth.models import User
from principal.models import Posts_Model

# Create your views here.
def create_post(request):
    """View que se encargará de manejar y recibir los datos ingresados en un formulario para crear una publicación.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.

    Returns:
        render/redirect: devolverá el renderizado de la página web con el formulario para rellenar y una redirección al crear el post.
    """
    actual_user = User.objects.get(pk=request.user.pk) #De esta manera obtengo el usuario actual que está creando la publicación

    if request.method == 'POST': 
        create_post_form = Create_Post(data=request.POST) #almaceno los datos obtenidos del formulario 

        if create_post_form.is_valid():
            new_post = create_post_form.save(commit=False) #aún no realizo el commit a la bbdd ya que me hace falta almacenar tambien el id del usuario
            new_post.posted_by = actual_user
            new_post.save()

            messages.success(request, 'Publicación Creada!') #Mensaje Feedback exitoso

            return redirect('all_posts')
    else:
        create_post_form = Create_Post() #Instancio el formulario en espera de ingresar datos

    return render(request, 'posting_templates/create_post.html', {'form':create_post_form})

def likes(request, id):
    """Función que se encargará de dar like a las publicaciones y verificar si ya se ha realizado dicha acción o si se ha dado dislike.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        id (int): id del post.

    Returns:
        redirect: redireccionará a la página de todas las publicaciones
    """
    #query:
    post = Posts_Model.objects.get(id=id)
    
    if request.user.is_authenticated: #verifico que el usuario esté logeado
        is_dislike = False
        for dislike in post.down_voted.all(): #busco en mi bbdd si el usuario ya dió dislike en la publicación
            if dislike == request.user:
                is_dislike = True
                break #se deja de buscar el usuario una vez obtenido

        if is_dislike: #si es así se elimina el dislike para dar paso al like
            post.down_voted.remove(request.user)

        is_like = False
        for like in post.up_voted.all(): #realizo la misma busqueda para saber si el usuario ya dió like en la publicación
            if like == request.user:
                is_like = True
                break #se deja de buscar el usuario

        if not is_like: #si no ha dado like, se agrega
            post.up_voted.add(request.user)
        
        if is_like: #si ya lo ha dado, se elimina el dato del usuario que ha dado like
            post.up_voted.remove(request.user)

    else:
        messages.error(request, 'Necesitas Iniciar Sesión para Indicar que te Gusta la Publicación.')

    return redirect('all_posts')

def dislikes(request, id):
    """Función que se encargará de dar dislike a las publicaciones y verificar si ya se ha realizado dicha acción o si se ha dado like.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        id (int): id del post.

    Returns:
        redirect: redireccionará a la página de todas las publicaciones
    """
    #query:
    post = Posts_Model.objects.get(id=id)

    if request.user.is_authenticated:
        is_like = False
        for like in post.up_voted.all():
            if like == request.user:
                is_like = True
                break
            
        if is_like:
            post.up_voted.remove(request.user)

        is_dislike = False
        for dislike in post.down_voted.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike: 
            post.down_voted.add(request.user)
        
        if is_dislike:
            post.down_voted.remove(request.user)

    else:
        messages.error(request, 'Necesitas Iniciar Sesión para Indicar que no te Gusta la Publicación.')

    return redirect('all_posts')

def delete_post(request, slug):
    """Función que dará el permiso a un usuario de eliminar sus propias publicaciones realizadas.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        slug (string): se enviará el SlugField para identificar el post a eliminar.

    Returns:
        redirect: redireccionará a la página de todas las publicaciones.
    """
    #query:
    post = Posts_Model.objects.get(slug=slug) 
    
    if request.user == post.posted_by: #solo se dará permiso a que los usuarios eliminen sus propias publicaciones
        post.delete() #en caso de ser True la verificación, se elimina el post
        
        messages.success(request, 'Publicación Eliminada')
    else:
        messages.error(request, 'No eres el propietario de esta publicación.')

    return redirect('all_posts')