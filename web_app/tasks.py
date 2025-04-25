from celery import shared_task
from django.core.mail import send_mail

@shared_task
def enviar_notificacion_cita(codigo, medico_email, paciente_email, medico_nombre, paciente_nombre, fecha, hora, ciudad, sede, consultorio, estado):
    asunto = f'Cita médica agendada - Código {codigo}'
    mensaje = (
        f'Hola, se ha agendado una cita médica.\n\n'
        f'Médico: {medico_nombre}\n'
        f'Paciente: {paciente_nombre}\n'
        f'Fecha: {fecha} a las {hora}\n'
        f'Ciudad: {ciudad} | Sede: {sede} | Consultorio: {consultorio}\n'
        f'Estado: {estado}\n'
    )
    send_mail(
        asunto,
        mensaje,
        'chdsistemas@gmail.com',
        [medico_email, paciente_email],
        fail_silently=False,
    )


