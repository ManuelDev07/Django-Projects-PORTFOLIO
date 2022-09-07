from django.shortcuts import render, redirect
from .models import Comments_Model, Category_Model, Console_Model, Posts_Model, Genres_Model
from conf_posts.forms import Comment_Post_Form
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def all_posts(request):
    """View que se encargará de mostrar todas las publicaciones del blog.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.

    Returns:
        render: devolverá el renderizado de la página web con los datos solicitados.
    """

    #query:
    posts = Posts_Model.objects.all()

    #menú:
    categories = Category_Model.objects.all()
    consoles = Console_Model.objects.all()

    return render(request, 'principal_templates/all_posts.html', {
        'posts':posts, 
        'categories':categories, 
        "consoles":consoles
    })

def category_posts(request, slug):
    """View que se encargará de mostrar todas las publicaciones que formen parte de una categoría del blog.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        slug (string): recibirá el dato SlugField.

    Returns:
        render: devolverá el renderizado de la página web con los datos solicitados.
    """

    category = Category_Model.objects.get(slug=slug)
    posts = Posts_Model.objects.filter(category=category)

    #menú:
    categories = Category_Model.objects.all()
    consoles = Console_Model.objects.all()

    return render(request, 'principal_templates/genres_categories_consoles_posts.html', {
        'posts':posts, 
        'categories':categories, 
        "consoles":consoles,
        "title":slug,
    })

def genre_posts(request, slug):
    """View que se encargará de mostrar todas las publicaciones que formen parte de un género de videojuegos del blog.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        slug (string): recibirá el dato SlugField para hacer el filtro.

    Returns:
        render: devolverá el renderizado de la página web con los datos solicitados.
    """

    #query:
    genre = Genres_Model.objects.get(slug=slug)
    posts = Posts_Model.objects.filter(genre=genre)

    #menú:
    categories = Category_Model.objects.all()
    consoles = Console_Model.objects.all()

    return render(request, 'principal_templates/genres_categories_consoles_posts.html', {
        'posts':posts, 
        'categories':categories, 
        "consoles":consoles,
        "title":slug,
    })

def consoles_posts(request, slug):
    """View que se encargará de mostrar todas las publicaciones que formen parte de una consola del blog.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        slug (string): recibirá el dato SlugField para hacer el filtro.

    Returns:
        render: devolverá el renderizado de la página web con los datos solicitados.
    """

    #query:
    console_name = Console_Model.objects.get(slug=slug)
    posts = Posts_Model.objects.filter(console_name=console_name)

    #menú:
    categories = Category_Model.objects.all()
    consoles_names = Console_Model.objects.all()

    return render(request, 'principal_templates/genres_categories_consoles_posts.html', {
        'posts':posts, 
        'categories':categories, 
        "consoles":consoles_names,
        "title":slug.title(),
    })

def detailed_post(request, slug, pk):
    """View que se encargará de mostrar toda la información en detalle de una publicación, junto con la casilla de comentarios,
    la opción de eliminar blog.

    Args:
        request (HTTP): petición HTTP que se recibirá desde la web.
        slug (string): recibirá el dato SlugField del post para hacer el filtro.
        pk (int): recibirá tanto el id del post como del usuario para identificar.

    Returns:
        render/redirect: devolverá el renderizado de la página web con los datos solicitados o un redirect al realizar un comentario 
        en la publicación.
    """

    #query para mostrar la publicación en detalle y el usuario que comentará:
    post = Posts_Model.objects.get(pk=pk)
    user = User.objects.get(pk=request.user.pk)

    if request.method == 'POST': #verifico el método de la petición
        comment_form = Comment_Post_Form(data=request.POST) #Instancio y almaceno los datos del formulario

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) #aún no guado los datos
            new_comment.title_id = post.id #asigno los id del comentario con el id de la publicación
            new_comment.commented_by_id = user.id #asigno el id del usuario para mostrar quien fué el que comentó
            new_comment.save()

            messages.success(request, 'Comentario Publicado!') #Mensaje Feedback exitoso

            return redirect('all_posts')
    else:
        comment_form = Comment_Post_Form()

    #Query para obtener y mostrar los comentarios de la publicación:
    title = Posts_Model.objects.get(slug=slug)
    comments = Comments_Model.objects.filter(title=title)

    return render(request, 'principal_templates/detailed_post.html', {
        'post':post, 
        "title":post.title.title(), 
        "form":comment_form, 
        "comments_posted":comments
    })