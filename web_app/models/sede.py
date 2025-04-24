from django.db import models

class Sede(models.Model):
    codigo = models.CharField(max_length=100, unique=True, verbose_name='Código de la sede médica')
    nombre = models.CharField(max_length=200, verbose_name='Sede de prestación del servicio médico')
    ciudad = models.CharField(max_length=150, verbose_name='Ciudad de asentamiento de la sede', default='SOACHA')
    direccion = models.CharField(max_length=150, verbose_name='Direccion de la sede', default='0')
    telefono = models.CharField(max_length=150, verbose_name='Teléfono de contacto', default='0')
    descripcion = models.TextField(verbose_name='Descripción de la sede', default='0')

    class Meta:
        db_table = 'sedes'

    def __str__(self):
        return (f'{self.nombre} - {self.ciudad}')
    
    