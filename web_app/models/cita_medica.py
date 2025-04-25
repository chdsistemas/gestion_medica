from django.db import models
from web_app.models.medico import Medico
from web_app.models.paciente import Paciente
from web_app.models.sede import Sede
from datetime import datetime
import time
from django.core.exceptions import ValidationError


class CitaMedica(models.Model):
    ESTADO = [
        ('AG', 'AGENDADA'),
        ('AT', 'ATENDIDA'),
        ('CA', 'CANCELADA'),
        ('NA', 'NO ATENDIDA')
    ]
    codigo = models.CharField(max_length=50, blank=True, unique=True, verbose_name='Código de la cita', editable=False)
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, related_name='citas')
    consultorio = models.CharField(max_length=50, blank=False, verbose_name='Consultorio', default='101')
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='citas_medicas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='citas_medicas')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, blank=False, verbose_name='Estado de la cita', choices=ESTADO, default='AGE')

    
    class Meta:
        db_table = 'citas_medicas'
    

    def __str__(self):
        return f'{self.codigo} - {self.medico.first_name} - {self.medico.last_name} - {self.paciente.first_name} - {self.paciente.last_name}'
    

    # El método nativo clean() del modelo, se usa para validar datos, en este caso la fecha y hora de la cita
    # Debemos combinar la fecha y hora de nuestro modelo para validar citas en el futuro

    def clean(self): 
        fecha_hora_cita = datetime.combine(self.fecha, self.hora)
        este_momento = datetime.now() # Hora de Colombia

        if fecha_hora_cita < este_momento:
            raise ValidationError('La fecha y hora no corresponden, verique de nuevo...')


    def save(self, *args, **kwargs):
        if not self.codigo:
            tiempo = int(time.time() * 1000)  # Marca entera de la fecha hora actual en ms
            self.codigo = f'GEN-{tiempo}'# Código único basado en la fechahora actual
        super().save(*args, **kwargs)