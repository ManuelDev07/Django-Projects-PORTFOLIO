from principal.models import Posts_Model, Comments_Model
from django import forms

#Formularios para la creación de Publicaciones
class Create_Post(forms.ModelForm):
    class Meta:
        model = Posts_Model #Instancio el Modelo
        fields = ["title", "image", "content", 'category', "genre", "console_name"] #campos/input del Form

#Formularios para poder realizar comentarios en las Publicaciones
class Comment_Post_Form(forms.ModelForm):
    class Meta:
        model = Comments_Model
        fields = ['comment'] 