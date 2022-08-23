from django.db import models

# Create your models here.
class To_Do_Model(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='Título de la Tarea')
    desc = models.CharField(max_length=555, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creada el')
    done = models.BooleanField(default=False, verbose_name='¿Completada?')
    removed_or_not = models.BooleanField(default=False, verbose_name='¿Eliminada?')

    class Meta:
        verbose_name = 'Tarea'
        verbose_name = 'Tareas'

    def __str__(self) -> str:
        return self.title