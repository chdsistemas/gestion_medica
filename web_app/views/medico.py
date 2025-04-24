from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from web_app.forms.medico import MedicoForm
from web_app.models.medico import Medico
from django.contrib.auth import update_session_auth_hash



def registrar_medico(request):
    if request.method == 'POST':
        formulario = MedicoForm(request.POST, request.FILES)
        if formulario.is_valid():
            medico = formulario.save(commit=False)
            # Cifra la contraseña utilizando set_password()
            medico.set_password(formulario.cleaned_data['password'])
            medico.save()
            messages.success(request, 'Médico creado exitosamente.')
            return redirect('registrar_medico')  # Cambia esto a la URL que desees redirigir
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = MedicoForm()
    return render(request, 'medico/insertar.html', {'formulario': formulario})



def listar_medicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medico/listar.html', {'medicos':medicos})


@login_required
def actualizar_medico(request):
    usuario = request.user  # Usuario autenticado

    try:
        medico = Medico.objects.get(pk=usuario.pk)  # Obtener perfil de médico
    except Medico.DoesNotExist:
        messages.error(request, "No tienes un perfil de médico registrado.")
        return redirect('home')

    if request.method == 'POST':
        formulario = MedicoForm(request.POST, request.FILES, instance=medico)  # Formulario de Médico

        if formulario.is_valid():
            medico = formulario.save(commit=False)  # No guardar aún en la BD

            # Cifrado de la nueva contraseña si se proporciona
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                medico.set_password(nueva_password)  # Cifra la contraseña correctamente
            
            medico.save()  # Guarda médico en BD
            
            update_session_auth_hash(request, request.user)  # Mantener sesión activa tras cambio de contraseña

            messages.success(request, "Perfil médico actualizado exitosamente.")
            return redirect('perfil_medico')
        else:
            messages.error(request, "Hay errores en el formulario.")
    else:
        formulario = MedicoForm(instance=medico)
    return render(request, 'medico/actualizar.html', {'formulario': formulario})


@login_required
def ver_perfil_medico(request):
    medico = request.user.medico  # Ver una plantilla del médico
    return render(request, 'medico/detallar.html', {'medico': medico})


def eliminar_medico(request, medico_id):
    medico = get_object_or_404(Medico, id = medico_id)
    medico.delete()
    return redirect('listar_medicos')


