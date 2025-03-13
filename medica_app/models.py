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

               
#endregion

class Medico(Usuario):
    numero_carnet = models.CharField(max_length=20, verbose_name='Carnet') 
    especialidad = models.CharField(max_length=150, verbose_name='Especialidad')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    
    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.is_active = False
            self.rol = 'MED'
        super().save(*args, **kwargs)



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
    
    
    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo asignar si el objeto es nuevo
            self.rol = 'PAC'
            self.is_active = True
        super().save(*args, **kwargs)



class AdministradorSistema(Usuario):
    ACCIONES = [('GU', 'Gestionar usuarios del sistema'), ('GS', 'Gestionar servicios de la entidad')]
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



class AuxiliarAdministrativo(Usuario):
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.fist_name} - {self.usuario.last_name}'



class AuxiliarEnfermeria(Usuario):
    DEPARTAMENTO = [
        ('URGENCIAS', 'URGENCIAS'),
        ('CONSULTA EXTERNA', 'CONSULTA EXTERNA'),
        ('OBSTETRICIA', 'OBSTETRICIA')
        ]
    departamento = models.CharField(max_length=20, choices=DEPARTAMENTO, default='CONSULTA EXTERNA')

    def __str__(self):
        return f'{self.usario.fist_name} - {self.usario.last_name}'

class CitaMedica(models.Model):
    ESTADO = [
        ('AG', 'AGENDADA'),
        ('AT', 'ATENDIDA'),
        ('CA', 'CANCELADA'),
        ('NA', 'NO ATENDIDA')
    ]
    codigo = models.CharField(max_length=50, blank=False, unique=True, verbose_name='Código de la cita')
    ciudad = models.CharField(max_length=50, blank=False, verbose_name='Ciudad')
    direccion = models.CharField(max_length=50, blank=False, verbose_name='Direccion')
    consultorio = models.CharField(max_length=50, blank=False, verbose_name='Consultorio', default='101')
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT, related_name='citas_medicas')
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT, related_name='citas_medicas')
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, blank=False, verbose_name='Estado de la cita', choices=ESTADO, default='AGENDADA')

    def __str__(self):
        return f'{self.codigo} - {self.paciente.first_name} - {self.paciente.last_name}'



class AgendaMedica(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='turnos')
    fecha = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    turno_disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.medico.first_name} - {self.medico.last_name}'





