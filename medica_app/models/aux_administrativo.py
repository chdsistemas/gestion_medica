from django.db import models
from medica_app.models.usuario import Usuario


class AuxiliarAdministrativo(Usuario):
    fecha_ingreso = models.DateField(auto_now_add=True)

    
    class Meta:
        db_table = 'aux_administrativos'
    

    def __str__(self):
        return f'{self.usuario.fist_name} - {self.usuario.last_name}'

