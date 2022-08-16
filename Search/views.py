from django.shortcuts import render
from django.contrib import messages
from Store.models import Manga, Author, Genre, Demography

# Create your views here.
def search_manga(request):
    """Función que permitirá al usuario usar el input de búsqueda y buscar el nombre de un manga.

    Args:
        request (HTTP): Petición HTTP

    Returns:
        render: devolverá el renderizado de la página con un listado de mangas que estén relacionados al texto ingresado.
    """

    if request.GET['search']: #Si la barra de búsqueda NO ESTÁ vacía

        text = request.GET['search'] #obtengo el string ingresado en el input
        
        #verifico que sea mayor a tres para mejores resultados
        if len(text) < 3:
            messages.error(request, 'Texto ingresado muy corto. Intenta de nuevo...')

            return render(request, 'results_search.html')

        else: #caso contrario que el string sea mayor
            results = Manga.objects.filter(name__icontains=text) #realizo un query en mi modelo de mangas con el texto ingresado por el usuario

            return render(request, 'results_search.html', {
                    'results':results, 
                    'query':text.title(),})

    else: #caso contrario si la barra ESTÁ vacía
        messages.error(request, 'Búsqueda Vacía... 💀')

        return render(request, 'results_search.html')

'''def search_author(request):
    #Para los menús:
    davailables_demographies = Demography.objects.filter(available=True)
    availables_genres = Genre.objects.filter(available=True) 

    #Búsqueda:
    if request.GET['search']:

        text = request.GET['search']
        if len(text) < 3:
            messages.error(request, 'Texto ingresado muy corto. Intenta de nuevo...')

            return render(request, 'inicio')

        else:
            results = Author.objects.filter(name__icontains=text)

        return render(request, 'results_search.html', {
            'results':results, 
            'query':results,
            'davailables_demographies':davailables_demographies,
            'availables_genres':availables_genres})
    else:
        messages.error(request, 'No hubo resultados')

        return render(request, 'inicio')

def search_genre(request):
    #Para los menús:
    davailables_demographies = Demography.objects.filter(available=True)
    availables_genres = Genre.objects.filter(available=True) 

    #Búsqueda:    
    if request.GET['search']:

        text = request.GET['search']
        if len(text) < 3:
            messages.error(request, 'Texto ingresado muy corto. Intenta de nuevo...')

            return render(request, 'inicio')

        else:
            results = Genre.objects.filter(genre__icontains=text)

        return render(request, 'results_search.html', {
            'results':results, 
            'query':results,
            'davailables_demographies':davailables_demographies,
            'availables_genres':availables_genres})
    else:
        messages.error(request, 'No hubo resultados')

        return render(request, 'inicio')

def search_demography(request):
    #Para los menús:
    davailables_demographies = Demography.objects.filter(available=True)
    availables_genres = Genre.objects.filter(available=True) 

    #Búsqueda:    
    if request.GET['search']:

        text = request.GET['search']
        if len(text) < 3:
            messages.error(request, 'Texto ingresado muy corto. Intenta de nuevo...')

            return render(request, 'inicio')

        else:
            results = Demography.objects.filter(demography__icontains=text)

        return render(request, 'results_search.html', {
            'results':results, 
            'query':results,
            'davailables_demographies':davailables_demographies,
            'availables_genres':availables_genres})
    else:
        messages.error(request, 'No hubo resultados')

        return render(request, 'inicio')
'''