from django.db import models
from django.utils.text import slugify

# Create your models here.
class Genre(models.Model):
    genre = models.CharField(max_length=80, unique=True, verbose_name='Género')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    available = models.BooleanField(default=True, verbose_name='¿Disponible?')

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.genre)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.genre

class Demography(models.Model):
    demography = models.CharField(max_length=80, unique=True, verbose_name='Demografía')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    available = models.BooleanField(default=True, verbose_name='¿Disponible?')

    class Meta:
        verbose_name = 'Demografía'
        verbose_name_plural = 'Demografías'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.demography)
        super(Demography, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.demography

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre del Autor')
    photo = models.ImageField(upload_to='author_photos', blank=True, null=True, verbose_name='Foto del Autor')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Author, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Manga(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre del Manga')
    original_name = models.CharField(max_length=255, verbose_name='Nombre Original del Manga')
    description = models.CharField(max_length=555, verbose_name='Descripción/Sinopsis')
    image = models.ImageField(upload_to='portadas',verbose_name='Portada del Manga')
    year = models.CharField(max_length=6, verbose_name='Año')
    price = models.FloatField(blank=False, null=False, default=0, verbose_name='Precio')
    state = models.BooleanField(default=True, verbose_name='Estado') #(True = En curso/False = Finalizado)
    country = models.CharField(max_length=50, verbose_name='País')
    recommended_age = models.CharField(max_length=30, verbose_name='Edad Recomendada')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Autor')
    genre = models.ManyToManyField(Genre)
    demography = models.ManyToManyField(Demography)
    available = models.BooleanField(default=True, verbose_name='¿Disponible?')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Manga'
        verbose_name_plural = 'Mangas'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Manga, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name