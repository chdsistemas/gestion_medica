from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from web_app.models.cita_medica import CitaMedica

@receiver(post_save, sender=CitaMedica)
def notificar_cita_creada(sender, instance, created, **kwargs):
    if created:
        print('Señal ejecutada con past_save')
        asunto = f"Cita médica agendada - Código {instance.codigo}"
        
        mensaje = (
            f'Cordial saludo, se ha agendado una cita médica.\n\n'
            f'Médico: {instance.medico.get_full_name()}\n'
            f'Paciente: {instance.paciente.get_full_name()}\n'
            f'Fecha: {instance.fecha} a las {instance.hora}\n'
            f'Sede: {instance.sede.nombre} | Consultorio: {instance.consultorio}\n'
            f'Estado: {instance.get_estado_display()}\n'
        )

        correos_destino = [correo for correo in [instance.medico.email, instance.paciente.email] if correo]

        send_mail(
            asunto,
            mensaje,
            'notificaciones_medical_cide@gmail.com',
            correos_destino,
            fail_silently=False,
        )
