from django.db import models
from web_app.models.orden_medica import OrdenMedica
from web_app.models.prestador import Prestador
from web_app.models.medico import Medico

class Autorizacion(models.Model):
    codigo = codigo = models.CharField(max_length=100, unique=True, verbose_name='Código de la autorización de servicios')
    orden_medica = models.OneToOneField(OrdenMedica, on_delete=models.PROTECT, related_name='autorizaciones')
    prestador = models.ForeignKey(Prestador, on_delete=models.PROTECT, related_name='autorizaciones')
    fecha = models.DateTimeField(auto_now_add=True)
    ESTADO = [
        ('PEN', 'Pendiente'),
        ('AUT', 'Autorizada'),
        ('REC', 'Rechazada')
    ]
    estado = models.CharField(max_length=10, verbose_name='Estado de la autorización', choices=ESTADO, default='PEN')
    descripcion = models.TextField(verbose_name='Descripcion y comentarios adjuntos')
    

    class Meta:
        db_table = 'autorizaciones'

    def __str__(self):
        return (f'Codigo de autorizacion: {self.codigo} - Orden médica: {self.orden_medica}')
    
