from django.db import models

class Prestador(models.Model):
    codigo = codigo = models.CharField(max_length=100, unique=True, verbose_name='Código del prestador de servicios médicos')
    nombre = models.CharField(max_length=100, unique=True, verbose_name='Nombre del prestador de servicios')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad de residencia del prestador de servicios')
    telefono = models.CharField(max_length=100, verbose_name='Teléfono del prestador de servicios')

    
    class Meta:
        db_table = 'prestadores'

    
    def __str__(self):
        return self.nombre
    
    