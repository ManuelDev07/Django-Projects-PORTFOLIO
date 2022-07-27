from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=100, verbose_name="nombre de usuario")
    first_name = models.CharField(max_length=150, verbose_name="Primer Nombre")
    email = models.EmailField(max_length=250, verbose_name="correo")
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Note(models.Model):
    title = models.CharField(verbose_name='Título', max_length=80)
    author = models.CharField(verbose_name='Autor', max_length=80, default='null')
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario', default=True)
    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

    def __str__(self):
        return self.title