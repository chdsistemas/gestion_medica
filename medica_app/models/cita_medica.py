from django.db import models
from medica_app.models.medico import Medico
from medica_app.models.paciente import Paciente


class CitaMedica(models.Model):
    ESTADO = [
        ('AG', 'AGENDADA'),
        ('AT', 'ATENDIDA'),
        ('CA', 'CANCELADA'),
        ('NA', 'NO ATENDIDA')
    ]
    codigo = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Código de la cita')
    ciudad = models.CharField(max_length=50, blank=False, verbose_name='Ciudad')
    direccion = models.CharField(max_length=50, blank=False, verbose_name='Direccion')
    consultorio = models.CharField(max_length=50, blank=False, verbose_name='Consultorio', default='101')
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='citas_medicas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='citas_medicas')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, blank=False, verbose_name='Estado de la cita', choices=ESTADO, default='AGENDADA')

    def __str__(self):
        return f'{self.codigo} - {self.paciente.first_name} - {self.paciente.last_name}'
    
