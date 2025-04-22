from django.db import models
from medica_app.models.especialidad import Especialidad
from medica_app.models.sede import Sede


class Consultorio(models.Model):
    codigo = models.CharField(max_length=50, verbose_name='Código del consultorio')
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name='consultorios')
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, related_name='consultorios')
    descripcion = models.CharField(max_length=50, verbose_name='Descripción del consultorio')


    class Meta:
        db_table = 'consultorios'

    
    def save(self, *args, **kwargs): # Cambiar la forma como se guardan los objetos de este modelo
        super().save(*args, **kwargs) # Primero se guarda el objeto y crea su llave primaria
        if not self.codigo: # Asignar un código personalizado al objeto
            self.codigo = f'CMED-{self.pk:20}' # Diez dígitos 


    def __str__(self):
        return (f'{self.codigo} - {self.especialidad}')
    
