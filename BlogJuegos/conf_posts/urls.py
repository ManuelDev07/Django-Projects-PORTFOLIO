from django.urls import path
from conf_posts import views

urlpatterns = [
    path('crear-publicacion/', views.create_post, name='create_post'),
    path('like/<int:id>/', views.likes, name='likes'),
    path('dislike/<int:id>/', views.dislikes, name='dislikes'),
    path('eliminar/<slug>/', views.delete_post, name='delete_post')
]