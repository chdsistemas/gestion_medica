
from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from medica_app.forms.paciente import PacienteForm
from medica_app.models.paciente import Paciente



def registrar_paciente(request):
    if request.method == 'POST':
        formulario = PacienteForm(request.POST, request.FILES)
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            # Cifra la contraseña utilizando set_password()
            paciente.set_password(formulario.cleaned_data['password'])
            paciente.save()
            messages.success(request, 'Paciente creado exitosamente.')
            return redirect('registrar_paciente')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = PacienteForm()
    return render(request, 'paciente/insertar.html', {'formulario': formulario})



def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/listar.html', {'pacientes':pacientes})



def detallar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'paciente/detallar.html', {'paciente':paciente})



def actualizar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)  # Obtiene el paciente a actualizar
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST, instance=paciente)  # Envía el paciente actual
        if formulario.is_valid():
            paciente = formulario.save(commit=False)
            # Si el usuario cambió la contraseña se cifra antes de pasarla al objeto
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                paciente.set_password(nueva_password)
            paciente.save()
            messages.success(request, 'Paciente actualizado exitosamente.')
            return redirect('detallar_paciente', paciente_id)
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = FormularioPaciente(instance=paciente)
    return render(request, 'paciente/actualizar.html', {'formulario': formulario})



def eliminar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id = paciente_id)
    paciente.delete()
    return redirect('listar_pacientes')


