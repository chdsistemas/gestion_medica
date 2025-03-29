from django.db import models
from medica_app.models.usuario import Usuario


class AdministradorSistema(Usuario):
    ACCIONES = [
        ('GU', 'Gestionar usuarios del sistema'), 
        ('GS', 'Gestionar servicios de la entidad')
        ]
    codigo = models.CharField(max_length=20)
    acciones = models.CharField(max_length=20, choices=ACCIONES, default='GU')
    profesion = models.CharField(max_length=100)
    fecha_ingreso = models.DateField()


    def habilitar_usuario(self, usuario):
        usuario.is_active = True
        usuario.save()


    def inhabilitar_usuario(self, usuario):
        usuario.is_active = True
        usuario.save()

        
    def save(self, *args, **kwargs):
        if not self.pk:
            self.rol = 'ADM'
            self.is_active = True  # Activar automáticamente
            self.set_password("CIDE2025*")  # Un password asignado por el sistema
        super().save(*args, **kwargs)