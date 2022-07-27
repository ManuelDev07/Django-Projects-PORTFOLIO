from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<int:categories_id>/', views.categories_posts_page, name='pagina_categoria'), #El nombre del parámetro debe ser igual a la columna de la BBDD
]