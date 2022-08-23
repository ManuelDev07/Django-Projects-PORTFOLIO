from django.urls import path
from .views import full_image
from Store import views

urlpatterns = [
    path('', views.store_manga, name='inicio'),
    path('genre-manga/<slug:slug>/', views.detail_genre, name='detalle_genero'),
    path('demography-manga/<slug:slug>/', views.detail_demographies, name='detalle_demografia'),
    path('author/<slug:slug>/', views.detail_authors, name='author'),
    path('manga/<slug:slug>/', views.detail_manga, name='manga'),
    path('image/<slug:slug>/', views.full_image, name='imagen')
]