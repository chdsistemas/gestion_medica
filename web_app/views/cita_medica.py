from web_app.forms.cita_medica import CitaMedicaForm
from web_app.models.cita_medica import CitaMedica
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404



@login_required
def registrar_cita_medica(request):
    if request.method == 'POST':
        formulario = CitaMedicaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cita médica creada exitosamente.')
            return redirect('registrar_cita')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = CitaMedicaForm()
    return render(request, 'cita_medica/insertar.html', {'formulario': formulario})




@login_required
def listar_citas_medicas(request):
    citas = CitaMedica.objects.all()
    return render(request, 'cita_medica/listar.html', {'citas': citas})



@login_required
def listar_mis_citas(request):
    usuario = request.user  # Usuario autenticado, puede ser médico, paciente, administrador de sistema, etc
    if  hasattr(usuario, 'medico'):
        citas = CitaMedica.objects.filter(medico_id = usuario) # Filtrar las citas médicas del médico logueado
    elif hasattr(usuario, 'paciente'):
        citas = CitaMedica.objects.filter(paciente_id = usuario) # Filtrar las citas médicas del paciente logueado
    else:
        return redirect('home')  # Redirigir si no es ni médico ni paciente
    return render(request, 'cita_medica/listar.html', {'citas': citas})



@login_required
def actualizar_cita_medica(request, cita_medica_id):
    cita_medica = get_object_or_404(CitaMedica, id=cita_medica_id)  # Obtiene el paciente a editar
    if request.method == 'POST':
        formulario = CitaMedicaForm(request.POST, instance=cita_medica)  # Envía el paciente actual
        if formulario.is_valid():
            cita_medica.save()
            messages.success(request, 'Cita médica actualizada exitosamente.')
            return redirect('listar_citas', cita_medica_id)
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = CitaMedicaForm(instance=cita_medica)
    return render(request, 'cita_medica/actualizar.html', {'formulario': formulario})



def eliminar_cita_medica(request, cita_medica_id):
    cita = get_object_or_404(CitaMedica, id=cita_medica_id)
    cita.delete()
    return redirect('listar_citas')
