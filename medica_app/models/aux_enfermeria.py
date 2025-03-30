from django.db import models
from medica_app.models.usuario import Usuario


class AuxiliarEnfermeria(Usuario):
    DEPARTAMENTO = [
        ('URG', 'URGENCIAS'),
        ('CEX', 'CONSULTA EXTERNA'),
        ('OBS', 'OBSTETRICIA')
        ]
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTO, default='CONSULTA EXTERNA')


    class Meta:
        db_table = 'aux_enfermeria'
        
    
    def __str__(self):
        return f'{self.usario.fist_name} - {self.usario.last_name}'
    
