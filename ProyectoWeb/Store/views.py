from django.shortcuts import render
from .models import Product, CategoryProduct

# Create your views here.
def store(request): #Página de la tienda
    #Guardo en una variable TODOS los datos de las tablas de productos y categorías:
    products = Product.objects.all()
    categories = CategoryProduct.objects.all()

    return render(request, 'store.html', {
        'products':products,
        'categories':categories
    })

def category_product_page(request, categories_id): #Página en detalle que mostrará TODOS los productos que pertenezcan a una categoría en específico:

    #Guardo en una variable el id de la categoria específica:
    category = CategoryProduct.objects.get(id=categories_id)
    products = Product.objects.filter(categories_id=category)#Filtro aquellos productos que formen parte de esa categoria

    #lista para el menú de categorías de esta página:
    categories = CategoryProduct.objects.all()

    return render(request, 'category_product_page.html', {
        'category':category, 
        'products':products,
        'categories':categories
    })