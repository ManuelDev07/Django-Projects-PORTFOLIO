from django.db import models

# Create your models here.
class Services(models.Model):
    #Campos de la Tabla Services
    title = models.CharField(max_length=80, verbose_name='Título')
    content = models.CharField(max_length=255, verbose_name='Contenido')
    
    #El upload_to indica que se guardará en una carpeta con el nombre de mi APP(Services)
    image = models.ImageField(upload_to='Services', verbose_name='Imagen')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models. DateTimeField(auto_now_add=True, verbose_name='Actualizado el')

    class Meta:#Nombres en singular/plural de la Tabla Services
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return f'Creado el: {self.created_at.day}/{self.created_at.month}/{self.created_at.year}'