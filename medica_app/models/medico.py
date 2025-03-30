from django.db import models
from medica_app.models.usuario import Usuario
from medica_app.models.especialidad import Especialidad


class Medico(Usuario):
    numero_carnet = models.CharField(max_length=20, verbose_name='Carnet') 
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, verbose_name='Especialidad Medica', related_name='especialidades')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    
    class Meta:
        db_table = 'medicos'

    
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = False
            self.rol = 'MED'
        super().save(*args, **kwargs)

        