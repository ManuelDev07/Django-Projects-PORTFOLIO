from django.shortcuts import render
from .models import Genre, Manga, Author, Demography
from django.core.paginator import Paginator

# Create your views here.
def store_manga(request):
    """Vista que será la página principal de la tienda, obteniendo todos los datos de los models para mostrarlos junto con un sistema de paginación.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página principal.
    """
    #Información General
    genres = Genre.objects.filter(available=True) 
    mangas = Manga.objects.filter(available=True)
    demographies = Demography.objects.filter(available=True)

    #Paginación:
    paginator = Paginator(mangas, 6) #Seis elementos por página

    #Números de Páginas:
    page = request.GET.get('page')
    pages = paginator.get_page(page)

    return render(request, 'store.html', {
        'genres':genres, 
        #'mangas':mangas, 
        'demographies':demographies,
        'mangas_pages':pages})

def detail_genre(request, slug):
    """Vista que mostrará ciertos mangas de un género en específico para una mejor búsqueda.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página de detalle de géneros/demografías/autores.
    """
    #Filtro de Géneros
    genre = Genre.objects.get(slug=slug)
    mangas = Manga.objects.filter(genre=genre)

    return render(request, 'detail_genre_demography.html', {'genre':genre,'mangas':mangas})

def detail_demographies(request, slug):
    """Vista que mostrará ciertos mangas de una demografía en específico para una mejor búsqueda.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página de detalle de géneros/demografías/autores.
    """
    #Filtro de Demografías:
    demographies = Demography.objects.get(slug=slug)
    mangas = Manga.objects.filter(demography=demographies)    

    return render(request, 'detail_genre_demography.html', {'demographies':demographies,'mangas':mangas})

def detail_authors(request, slug):
    """Vista que mostrará ciertos mangas de un autor en específico para una mejor búsqueda.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página de detalle de géneros/demografías/autores.
    """    
    #Filtro de Autores:
    authors = Author.objects.get(slug=slug)
    mangas = Manga.objects.filter(author=authors)

    return render(request, 'detail_genre_demography.html', {'authors':authors,'mangas':mangas})

def detail_manga(request, slug):
    """Vista que mostrará la información más completa y detallada de un manga en específico.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página de detalle de un solo manga.
    """
    #Obtengo el manga que será mostrado en detalle:
    manga = Manga.objects.get(slug=slug)

    return render(request, 'detail_manga.html', {'manga':manga})

def full_image(request, slug):
    """Vista que mostrará solamente la imagen de la portada de un manga.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el jpg/png del manga.
    """
    #obtengo el manga para luego mostrar su imagen en el HTML
    image = Manga.objects.get(slug=slug)

    return render(request, 'full_image.html', {
        'image':image})