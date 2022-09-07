from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.
class Category_Model(models.Model):
    "Modelo para las categorías que tendrá cada Publicación"
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Categoría')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self) -> str:
        return self.name

class Console_Model(models.Model):
    "Modelo para las consolas a las que se referirán en la Publicación"
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre de la Consola')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Consola'
        verbose_name_plural = 'Consolas'

    def __str__(self) -> str:
        return self.name

class Genres_Model(models.Model):
    "Modelo para los géneros de los videojuegos que abarcará las publicaciones"
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre del Género del Juego')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Género del Juego'
        verbose_name_plural = 'Géneros de los Juegos'

    def __str__(self) -> str:
        return self.name

class Posts_Model(models.Model):
    "Modelo que establece los datos que tendrá una Publicación (fields/campos)"
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='Título del Post')
    image = models.ImageField(null=True, blank=True, upload_to='images_posts', verbose_name='Imágen del Post')
    content = models.TextField(null=True, blank=True, db_column='content', editable=True, verbose_name='Contenido del Post')
    up_voted = models.ManyToManyField(User, related_name='likes')
    down_voted = models.ManyToManyField(User, related_name='dislikes')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    slug = models.SlugField(max_length=50, verbose_name='URL')

    #Relaciones:
    posted_by = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Publicado por')
    category = models.ManyToManyField(Category_Model, verbose_name='Categorías')
    genre = models.ManyToManyField(Genres_Model, verbose_name='Géneros')
    console_name = models.ManyToManyField(Console_Model, verbose_name='Consolas')
    
    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
    
    def save(self, *args, **kwargs): #Establezco que cada que se cree una publicación se genere un SlugField automático
        self.slug = slugify(self.title)
        super(Posts_Model, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

class Comments_Model(models.Model):
    "Modelo que funcionará para los comentarios de las publicaciones"
    title = models.ForeignKey(Posts_Model, on_delete=models.CASCADE, verbose_name='Título de la Publicación Comentada')
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Comentario de')
    comment = models.CharField(max_length=555, verbose_name='Comentario')
    commented_on = models.DateTimeField(auto_now_add=True, verbose_name='Comentado el')

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self) -> str:
        return self.comment