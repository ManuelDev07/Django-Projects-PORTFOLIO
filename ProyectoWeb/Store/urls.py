from django.urls import path
from Store import views

urlpatterns = [
    path('', views.store, name='tienda'),
    path('category-product/<int:categories_id>', views.category_product_page, name='productos_de_una_categoria')
]