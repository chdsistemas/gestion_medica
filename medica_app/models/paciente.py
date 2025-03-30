from django.db import models
from medica_app.models.usuario import Usuario

class Paciente(Usuario):
    TIPO = [
        ('ESTANDAR', 'ESTANDAR'),
        ('PREMIUM', 'PREMIUM')
    ]
    GENERO = [
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO')
    ]
    tipo = models.CharField(max_length=50, blank=False, verbose_name='Tipo de paciente', choices=TIPO, default='ESTANDAR')
    genero = models.CharField(max_length=50, blank=False, verbose_name='Género de paciente', choices=GENERO, default='FEMENINO')
    
    
    class Meta:
        db_table = 'pacientes'
        
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.rol = 'PAC'
            self.is_active = True
        super().save(*args, **kwargs)
