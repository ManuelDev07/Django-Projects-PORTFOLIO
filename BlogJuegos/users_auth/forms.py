from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register_Form(UserCreationForm):
    "Formulario para el Registro de usuarios"
    
    class Meta:
        model = User #instancio el modelo a usar
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2'] #campos que quiero mostrar en mi formulario