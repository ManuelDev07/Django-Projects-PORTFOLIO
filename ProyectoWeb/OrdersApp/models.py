from django.db import models
from django.contrib.auth import get_user_model #Esto es para que me devuelva el usuario actual (que está logeado y está realizando el carrito junto con el pedido)
from Store.models import Product #Para poder acceder a los datos del producto para la Tabla 'OrderLine'
from django.db.models import F, Sum, FloatField #Esto es para calcular el precio total de la orden del pedido

User = get_user_model() #Obtengo el usuario activo mediante una variable

#Este modelo se trabajará con dos tablas relacionadas:

# Create your models here.
class Order(models.Model):
    #Esta tabla será los datos del pedido que habrá hecho x usuario (recordar qeu el id del pedido lo formará el programa automáticamente)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Pedido Creado el')
    
    #Campo relacionado a la tabla de User para acceder al id del usuario que realiza el pedido
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id del Usuario') #id del Usuario que ha Hecho el Pedido

    class Meta:
        db_table = 'Orders' #El nombre que tendrá la tabla en mi BBDD
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id'] #Quiero que se ordene por id

    def __str__(self):
        return f'Pedido Nro: {self.id}' #Devolverá el id del pedido

    @property
    def total_price(self): #El total del pedido
        return self.OrderLine_set.aggregate(total = Sum(F('price')*F('quantity'), output_field=FloatField()))['Total'] #Nombre del campo


#Esta tabla tendrá los datos de cada producto que forman parte del pedido
class OrderLine(models.Model):
    quantity = models.IntegerField(verbose_name='Cantidad', default=1) #cantidad de cada artículo
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    
    #Este campo estará relacionado a la tabla Order ya que tendrá el id de ese pedido
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='id del Pedido')
    
    #Campo relacionado a la tabla de Product de la app 'Store' para acceder al id del producto
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='id del Producto')

    #Campo relacionado a la tabla de User para acceder al id del usuario que realiza el pedido
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id del Usuario')

    class Meta:
        db_table = 'OrderLine'
        verbose_name = 'Línea del Pedido'
        verbose_name_plural = 'Líneas de los Pedidos'
        ordering = ['id']
    
    def __str__(self):
        return f'{self.quantity} -> {self.product.name}.'