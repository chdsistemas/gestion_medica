from django.db import models
import os
import logging
from django.contrib.auth.models import AbstractUser


# Destinar una carpeta en el sistema de archivos para subir documentos
def user_directory_path(instance, filename):
    return f"usuario/{instance.id}_{filename}"


# Configuración del logger
logger = logging.getLogger(__name__)



class Usuario(AbstractUser):
    TIPO_DOC = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cédula de Extranjería')
    ]
    ROL = [
        ('MED', 'Medico'),
        ('PAC', 'Paciente'),
        ('AUXA', 'Auxiliar Administrativo'),
        ('AUXE', 'Auxiliar Enfermeria'),
        ('ADM', 'Administrador de Sistema'),
        ('ND', 'No asignado')
    ]
    tipo_doc = models.CharField(max_length=3, blank=False, default='CC', choices=TIPO_DOC, verbose_name='Tipo de documento de identidad')
    num_doc = models.CharField(max_length=20, blank=False, unique=True, verbose_name='Número de documento')
    fecha_nac = models.DateField(verbose_name='Fecha de nacimiento')
    ciudad_res = models.CharField(max_length=100, blank=False, default='SOACHA', verbose_name='Ciudad Residencia')
    direccion = models.CharField(max_length=100, blank=False, verbose_name='Dirección Residencia')
    telefono = models.CharField(max_length=50, blank=False, verbose_name='Teléfono')
    imagen = models.ImageField(upload_to=user_directory_path, blank=True, null=True, verbose_name='Imagen')
    rol = models.CharField(max_length=20, choices=ROL, default='ND', verbose_name='Rol en la empresa')


    # Personalizar cómo se guarda un usuario
    # Guardado de la imagen del usuario en la superclase usuario reescribiendo método save()
    def save(self, *args, **kwargs):
        if self.pk:
            usuario_antiguo = Usuario.objects.filter(pk=self.pk).first()
            if usuario_antiguo and usuario_antiguo.imagen and self.imagen != usuario_antiguo.imagen:
                usuario_antiguo.imagen.delete(save=False)  # Eliminar la imagen anterior

        super().save(*args, **kwargs)  # Guardar cambios en la base de datos


    
    # Eliminar la imagen del servidor si el usuario se borra
    def delete(self, *args, **kwargs):
        if self.imagen and self.imagen.name:
            self.eliminar_imagen()
        super().delete(*args, **kwargs)



    def eliminar_imagen(self):
        try:
            # Se comprueba si hay una imagen y si hay ruta de acceso a ella en MEDIA_ROOT
            if self.imagen and self.imagen.name and os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
                logger.info(f"Imagen eliminada correctamente: {self.imagen.path}")
            else:
                logger.warning(f"La imagen no existe o n tiene un nombre válido: {self.imagen.path}")
        except Exception as e:
            logger.error(f"Error al eliminar la imagen {self.imagen.path}: {e}")