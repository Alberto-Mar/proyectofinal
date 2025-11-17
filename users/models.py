from django.db import models
from django.utils.timezone import now


class Hermano(models.Model):
    nombre = models.CharField(max_length=100)
    perimer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    correo = models.EmailField(unique=True, verbose_name='Correo Electrónico', nulll=True, blank=True)  # 


