from django.db import models
from django.contrib.auth.models import User #Esto es para la FK del campo "autor" de la tabla Post para relacionar las tablas

# Create your models here.
#Las entradas/posts del blog tendrá distintas categorias:
class Categories(models.Model):
    #Campos de la Tabla Categoria:
    name = models.CharField(max_length=80, verbose_name='Nombre de la Categoría')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return f'Categoría: {self.name}.'

#Post/Entradas del blog:
class Posts(models.Model):
    #Campos de la tabla de entradas del Post (donde tiene el contenido cada entrada)
    title = models.CharField(max_length=80, verbose_name='Título del Post')
    content = models.CharField(max_length=255, verbose_name='Contenido del Post')
    image = models.ImageField(upload_to='Blog', blank=True, null=True, verbose_name='Imágen') #Cada blog NO es obligatorio que tenga una imagen de portada y se subirá a una carpeta llamada "blog" dentro de la carpeta raíz media
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Post Creado el')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Post Actualizado el')
    
    #Se realizará una relación entre tablas:
    #El campo autor estará relacionado ya que puede crear varios post (UNO A VARIOS) entre el usuario y el POST
    #(on_delete=models.CASCADE) Para establecer que cuando se borre el usuario también deberán eliminarse sus posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor') #Se usa la clase User (la cual se importó)

    #Un post puede formar parte de una o más categorías O una categoría tiene varios Posts (MANY TO MANY)
    # Se crea el campo el cual estará relacionado a las categorias con ManyToManyField()
    #Dentro de los () se le indica a que clase(tabla) estará relacionada
    category = models.ManyToManyField(Categories)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Creado el: {self.created_at.day}/{self.created_at.month}/{self.created_at.year} a las {self.updated_at.hour}:{self.updated_at.minute}:{self.updated_at.second}.'