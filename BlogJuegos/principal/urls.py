from principal import views
from django.urls import path

urlpatterns = [
    path('todas-las-publicaciones/', views.all_posts, name='all_posts'),
    path("categoria/<slug>/", views.category_posts, name='category_posts'),
    path("genero/<slug>/", views.genre_posts, name='genre_posts'),
    path("consolas/<slug>/", views.consoles_posts, name='consoles_posts'),
    path('publicacion-detallada/<slug>/<int:pk>/', views.detailed_post, name='detailed_post')
]