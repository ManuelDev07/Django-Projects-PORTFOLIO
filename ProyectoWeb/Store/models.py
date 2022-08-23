from django.db import models

# Create your models here.
class CategoryProduct(models.Model):
    #Tabla con las categorías a las que pertenecerá cada producto creado:
    name = models.CharField(max_length=50, verbose_name='Nombre de la Categoría')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name = 'Categoría del Producto'
        verbose_name = 'Categorías de los Productos'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    #Tabla con los datos que tendrá cada producto:
    name = models.CharField(max_length=80, verbose_name='Nombre del Producto')
    price = models.FloatField(verbose_name='Precio')
    image = models.ImageField(upload_to='Store', verbose_name='Imagen del Producto')#La imagen será almacenada en la carpeta media/Store
    details = models.CharField(max_length=255, verbose_name='Detalles del Producto')
    
    #En este campo el valor default= hace que el valor por defecto de la casilla ¿Vendido? esté False
    sold = models.BooleanField(default=False, verbose_name='¿Vendido?')
    
    #El campo 'categories' estará relacionado a la tabla 'CategoryProduct' 
    categories = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'Publicado el {self.created_at.day}/{self.created_at.month}/{self.created_at.year}'