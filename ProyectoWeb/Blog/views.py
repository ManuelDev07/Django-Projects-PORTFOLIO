from django.http import Http404
from django.shortcuts import render
from Blog.models import Categories, Posts

# Create your views here.
def blog(request): #Página para el blog de usuarios
    #Guardo en una variable todo el contenido de las tablas (models.py) de la App Blog
    categories = Categories.objects.all()
    posts = Posts.objects.all()

    return render(request, 'blog.html', {'categories':categories, 'posts':posts})

def categories_posts_page(request, categories_id): #Página en detalle que mostrará los Post que pertenecen a una categoría en específico:
    
    #Guardo en una variable el id de la categoría y el post a la que quiero acceder
    category = Categories.objects.get(id=categories_id)
    posts = Posts.objects.filter(category=category) #Se usa filter para filtrar en base a la categoria id (lo que almacena la variable 'category')


    return render(request, 'category_page.html', {'category':category, 'posts':posts})