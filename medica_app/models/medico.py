from django.db import models
from medica_app.models.usuario import Usuario


class Medico(Usuario):
    numero_carnet = models.CharField(max_length=20, verbose_name='Carnet') 
    especialidad = models.CharField(max_length=150, verbose_name='Especialidad')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = False
            self.rol = 'MED'
        super().save(*args, **kwargs)