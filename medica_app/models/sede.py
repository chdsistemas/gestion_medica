from django.db import models

class Sede(models.Model):
    codigo = models.CharField(max_length=100, unique=True, verbose_name='Código de la sede médica')
    nombre = models.CharField(max_length=200, verbose_name='Sede de prestación del servicio médico')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción de la sede')

    class Meta:
        db_table = 'sedes'

    def __str__(self):
        return self.nombre
    
    