from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=55, verbose_name='Nombre')
    address = models.CharField(max_length=80, verbose_name='Dirección')
    email = models.EmailField(verbose_name='Dirección Correo Electrónico') #Si quiero que un campo no sea obligatorio, dentro de los () agrego blank=True, null=True
    phone_number = models.CharField(max_length=100, verbose_name='Número de Teléfono')

    def __str__(self): #Esto será lo que se verá en Admin Panel en el Modelo
        return f'Cliente: {self.name}'

class Articles(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    section = models.CharField(max_length=20, verbose_name='Sección')
    price = models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return f'El NOMBRE del articulo es: {self.name}, pertenece a la SECCIÓN: {self.section} y su PRECIO es de: {self.price}$.'

class Orders(models.Model):
    number = models.IntegerField(verbose_name='Número de Pedido')
    date = models.DateField(verbose_name='Fecha de Envío')
    received = models.BooleanField(verbose_name='¿Recibido?')

    def __str__(self):
        return f'Número de Pedido: {self.number}'
