from django.db import models


class Especialidad(models.Model):
    codigo =  models.CharField(max_length=20, unique=True, verbose_name='Codigo de la especialidad médica')
    nombre = models.CharField(max_length=200, unique=True, verbose_name='Nombre de la especialidad médica')
    descripcion = models.TextField(verbose_name='Descripción de la especialidad médica')

    class Meta:
        db_table = 'especialidades'

    def __str__(self):
        return self.nombre
    