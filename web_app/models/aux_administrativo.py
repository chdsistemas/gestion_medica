from django.db import models
from web_app.models.usuario import Usuario


class AuxiliarAdministrativo(Usuario):
    fecha_ing = models.DateField(verbose_name='Fecha de ingreso institucional', auto_now=True)

    
    class Meta:
        db_table = 'aux_administrativos'
    

    def __str__(self):
        return f'{self.usuario.fist_name} - {self.usuario.last_name}'
    
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto auxiliaradminisrativo es nuevo
            self.rol = 'AUXA'
            self.is_active = False
        super().save(*args, **kwargs)

