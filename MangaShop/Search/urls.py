from django.urls import path
from Search import views

urlpatterns = [
    path('search-manga/', views.search_manga, name='buscar-manga'),
]