from django.db import models


class OrdenMedica(models.Model):
    codigo = models.CharField(max_length=100, unique=True, verbose_name='Código de la orden médica')
    fecha_hora = models.TimeField(auto_now=True, verbose_name='Fecha y hora de emisióm')
    TIPO = [
        ('CON', 'Consulta médica'),
        ('PRO', 'Procedimientos'),
        ('MED', 'Medicamentos'),
        ('IMG', 'Imagenes de apoyo diagnóstico'),
        ('LAB', 'Laboratorios')
    ]
    descripcion = models.TextField(verbose_name='Descripción de la orden')
    autorizacion = models.BooleanField(verbose_name='¿Requiere autorización adicional?', default=False)
    PRIORIDAD = [
        ('NOR', 'Normal'), 
        ('URG', 'Urgencia')
        ]
    prioridad = models.CharField(max_length=15, verbose_name='Prioridad de la orden', choices=PRIORIDAD, default='NOR')
    ESTADO = [
        ('PEN', 'Pendiente'),
        ('TRA', 'En trámite'),
        ('ATE', 'Atendida'),
        ('CAN', 'Cancelada')
    ]
    estado = models.CharField(max_length=15, verbose_name='Estado de la orden', choices=ESTADO, default='PEN')

    