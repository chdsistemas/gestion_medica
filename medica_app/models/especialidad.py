from django.db import models


class Especialidad(models.Model):
    
    nombre = models.CharField(max_length=200, verbose_name='Nombre de la especialidad médica')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción de la especialidad médica')

    class Meta:
        db_table = 'especialidades'

    def __str__(self):
        return self.nombre
    