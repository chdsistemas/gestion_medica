from django.db import models
from medica_app.models.medico import Medico


class AgendaMedica(models.Model):
    # Queremos un código personalizado, consecutivo no modificable por el usuario
    codigo = models.CharField(max_length=20, unique=True, blank=True, null=True, editable=False)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    disponible = models.BooleanField( default=True)


    def save(self, *args, **kwargs): # Cambiar la forma como se guardan los objetos
        super().save(*args, **kwargs) #Primero se guarda el objeto y crea su llave primaria
        if not self.codigo:
            self.codigo = f'AG-{self.pk:20}' # Algunos dígitos 

    
    class Meta:
        db_table = 'agendas_medicas'


    def __str__(self):
        return f'{self.codigo} - {self.medico.first_name} - {self.medico.last_name}'
    
    