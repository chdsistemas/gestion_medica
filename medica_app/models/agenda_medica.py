from django.db import models
from medica_app.models.medico import Medico


class AgendaMedica(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    turno_disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.medico.first_name} - {self.medico.last_name}'
    
