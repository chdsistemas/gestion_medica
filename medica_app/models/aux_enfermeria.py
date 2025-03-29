from django.db import models
from medica_app.models.usuario import Usuario


class AuxiliarEnfermeria(Usuario):
    DEPARTAMENTO = [
        ('URGENCIAS', 'URGENCIAS'),
        ('CONSULTA EXTERNA', 'CONSULTA EXTERNA'),
        ('OBSTETRICIA', 'OBSTETRICIA')
        ]
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTO, default='CONSULTA EXTERNA')

    def __str__(self):
        return f'{self.usario.fist_name} - {self.usario.last_name}'
    