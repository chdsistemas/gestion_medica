from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from medica_app.forms import *
from medica_app.models import Medico, Paciente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import Http404, HttpResponse


def home(request):
    return render(request, 'home.html')



def inicio(request):
    tipo_usuario = None

    if request.user.is_authenticated:
        usuario_logueado = request.user
        if isinstance(usuario_logueado, Medico):
            tipo_usuario = 'Medico'
        elif isinstance(usuario_logueado, Paciente):
            tipo_usuario = 'Paciente'
        else:
            tipo_usuario = 'Usuario no identificado'

    return render(request, 'inicio.html', {'tipo_usuario': tipo_usuario})


# region usuario

def login_usuario(request):
    if request.method == 'POST':
        username_recibido = request.POST.get('username')
        password_recibido = request.POST.get('password')
        if not username_recibido or not password_recibido:
            return render(request, 'usuario/login.html', {'mensaje_error': 'Por favor, complete todos los campos.'})
        usuario = authenticate(request, username=username_recibido, password=password_recibido)
        if usuario is not None:
            login(request, usuario)
            # Verificar si el usuario es Médico u otros roles
            if hasattr(request.user, 'medico'):
                return render(request, 'medico/perfil.html', {'tipo_usuario': 'Medico'})
            elif hasattr(request.user, 'paciente'):
                return render(request, 'paciente/perfil.html', {'tipo_usuario': 'Paciente'})            
            elif hasattr(request.user, 'administradorsistema'):
                return render(request, 'administrador_s/perfil.html', {'tipo_usuario': 'Administrador de Sistema'})
            else:
                return render(request, 'usuario/perfil.html', {'tipo_usuario': 'Usuario sin rol en el sistema'})
        return render(request, 'usuario/login.html', {'mensaje_error': 'Credenciales incorrectas, intente de nuevo o consulte con Administrador de Sistema'})
    return render(request, 'usuario/login.html')


def logout_usuario(request):
    logout(request)
    return redirect('home')


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            usuario = formulario.save(commit=False) # Se crea un objeto usuario en memoria
            # Cifra la contraseña utilizando set_password()
            usuario.set_password(formulario.cleaned_data['password'])
            usuario.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('registrar_usuario')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = FormularioUsuario()
    return render(request, 'usuario/insertar.html', {'formulario': formulario})


@login_required
def actualizar_usuario(request):
    usuario = request.user  # Usuario logueado
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST, request.FILES, instance=usuario)  # Se incluye request.FILES
        if formulario.is_valid():
            usuario = formulario.save(commit=False)  # Aún no guardar en la BD
            nueva_password = formulario.cleaned_data.get('password')
            if nueva_password:
                usuario.set_password(nueva_password)
            # Si se subió una nueva imagen, actualizarla
            if 'imagen' in request.FILES:
                usuario.imagen = request.FILES['imagen']            
            # Si el usuario dejó el campo de imagen en blanco, eliminar la imagen
            elif not formulario.cleaned_data.get('imagen'):
                usuario.imagen = None  
            usuario.save()  # Ahora sí guardamos todo en la BD
            update_session_auth_hash(request, usuario)  # Mantiene la sesión activa después de actualizar la contraseña            
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('perfil_usuario')
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = FormularioUsuario(instance=usuario)
    return render(request, 'usuario/actualizar.html', {'formulario': formulario})



def listar_usuarios(request):
    usuarios = Usuario.objects.all().order_by('last_name')
    print(request)
    conteo = Usuario.objects.count()
    return render(request, 'usuario/listar.html', {'usuarios':usuarios, 'conteo': conteo})


@login_required
def listar_usuarios_filtrados(request):
    consultaSQL = request.GET.get('consultaSQL', '').strip()  # Obtener y limpiar la consulta del usuario
    usuarios = None  # Inicializar la variable usuarios

    if consultaSQL:  # Solo buscar si hay un valor en el campo
        usuarios = Usuario.objects.filter(first_name = consultaSQL)

        if not usuarios:
            messages.info(request, "No se encontraron usuarios con ese nombre.")  # Mensaje si no hay resultados

    return render(request, 'usuario/buscar.html', {'usuarios': usuarios, 'consultaSQL': consultaSQL})


@login_required
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id = usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')




@login_required
def ver_perfil_usuario(request):
    usuario = request.user.id  # Ver página el perfil del usuario
    return render(request, 'usuario/detallar.html', {'usuario': usuario})



@login_required
def detallar_usuario(request):
    usuario = request.user.id  # Ver los detalles del usuario
    return render(request, 'usuario/detallar.html', {'usuario': usuario })

# endregion


#region Medico

def registrar_medico(request):
    if request.method == 'POST':
        formulario = FormularioMedico(request.POST, request.FILES)
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
        formulario = FormularioMedico()
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
        formulario_medico = FormularioMedico(request.POST, request.FILES, instance=medico)  # Formulario de Médico

        if formulario_medico.is_valid():
            medico = formulario_medico.save(commit=False)  # No guardar aún en la BD

            # Cifrado de la nueva contraseña si se proporciona
            nueva_password = formulario_medico.cleaned_data.get('password')
            if nueva_password:
                medico.set_password(nueva_password)  # Cifra la contraseña correctamente
            
            medico.save()  # Guarda médico en BD
            
            update_session_auth_hash(request, request.user)  # Mantener sesión activa tras cambio de contraseña

            messages.success(request, "Perfil médico actualizado exitosamente.")
            return redirect('perfil_medico')
        else:
            messages.error(request, "Hay errores en el formulario.")
    else:
        formulario_medico = FormularioMedico(instance=medico)
    return render(request, 'medico/actualizar.html', {'formulario': formulario_medico})
    


@login_required
def ver_perfil_medico(request):
    medico = request.user.medico  # Ver una plantilla del médico
    return render(request, 'medico/detallar.html', {'medico': medico})



def eliminar_medico(request, medico_id):
    medico = get_object_or_404(Medico, id = medico_id)
    medico.delete()
    return redirect('listar_medicos')



#region paciente

def registrar_paciente(request):
    if request.method == 'POST':
        formulario = FormularioPaciente(request.POST, request.FILES)
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
        formulario = FormularioPaciente()
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
#endregion


#region Cita Medica
@login_required
def registrar_cita_medica(request):
    if request.method == 'POST':
        formulario = FormularioCitaMedica(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Cita médica creada exitosamente.')
            return redirect('registrar_cita')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = FormularioCitaMedica()
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
        formulario = FormularioCitaMedica(request.POST, instance=cita_medica)  # Envía el paciente actual
        if formulario.is_valid():
            cita_medica.save()
            messages.success(request, 'Cita médica actualizada exitosamente.')
            return redirect('listar_citas', cita_medica_id)
        else:
            messages.error(request, 'Hay errores en el formulario. Verifica los datos.')
    else:
        formulario = FormularioCitaMedica(instance=cita_medica)
    return render(request, 'cita_medica/actualizar.html', {'formulario': formulario})




def eliminar_cita_medica(request, cita_medica_id):
    cita = get_object_or_404(CitaMedica, id=cita_medica_id)
    cita.delete()
    return redirect('listar_citas')
#endregion


#region Administrador de Sistema
def registrar_administrador_sistema(request):
    if request.method == 'POST':
        formulario = FormularioAdministradorSistema(request.POST, request.FILES)
        if formulario.is_valid():
            administrador_s = formulario.save(commit=False) # Solo guardar el objeto en memoria, más tarde se guarda en la bd
            # Cifra la contraseña utilizando set_password()
            #administrador_s.set_password(formulario.cleaned_data['password'])
            administrador_s.save()
            messages.success(request, 'Administrador de sistema creado exitosamente.')
            return redirect('registrar_administrador_s')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = FormularioAdministradorSistema()
    return render(request, 'administrador_s/insertar.html', {'formulario': formulario})


@login_required
def listar_administradores_s(request):
    administradores_s = AdministradorSistema.objects.all()
    return render(request, 'administrador_s/listar.html', {'administradores_s': administradores_s})


@login_required
def gestionar_usuario(request):
    documento = request.GET.get('documento')  # Obtiene el número de documento ingresado
    usuario = None  # Inicializamos usuario en None para evitar errores en la plantilla
    if documento:
        try:
            usuario = Usuario.objects.get(num_doc=documento)
            messages.success(request, f'Usuario {usuario.num_doc} encontrado.')  # Mensaje de éxito
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')  # Mensaje de error
    return render(request, 'administrador_s/gestionar_usuario.html', {'usuario': usuario})


@login_required
def buscar_usuario_documento(request):
    documento = request.GET.get('documento')  # Obtiene el número de documento ingresado
    usuario = None  # Inicializamos usuario en None para evitar errores en la plantilla
    if documento:
        try:
            usuario = Usuario.objects.get(num_doc=documento)
            messages.success(request, f'Usuario {usuario.num_doc} encontrado.')  # Mensaje de éxito
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe.')  # Mensaje de error
    return render(request, 'administrador_s/buscar_documento.html', {'usuario': usuario})


@login_required
def buscar_usuarios_nombre(request):
    nombre = request.GET.get('nombre')  # Obtiene el nombre ingresado
    usuarios = Usuario.objects.none()  # Iniciar un queryset vacío
    if nombre:
        usuarios = Usuario.objects.filter(first_name__icontains=nombre)
        if usuarios.exists(): # Un método booleano de existencia de objetos
            messages.success(request, 'Usuario(s) encontrado(s).')  # Mensaje de éxito
        else:
            messages.error(request, 'La búsqueda no arrojó resultados.')  # Mensaje de error    
    return render(request, 'administrador_s/buscar_nombre.html', {'usuarios': usuarios})


@login_required
def usuario_por_parametros(request):
    criterio = request.GET.get('criterio')  # Obtiene el criterio de búsqueda
    a_buscar = request.GET.get('a_buscar')
    usuarios = Usuario.objects.none()  # Iniciar un queryset vacío
    if criterio:
        if criterio == 'nombre':
            usuarios = Usuario.objects.filter(first_name__icontains=a_buscar)
        elif criterio == 'apellido':
            usuarios = Usuario.objects.filter(last_name__icontains=a_buscar)
        elif criterio == 'documento':
            usuarios = Usuario.objects.filter(num_doc__iexact=a_buscar)
        elif criterio == 'activos':
            usuarios = Usuario.objects.filter(is_active=True)
        elif criterio == 'inactivos':
            usuarios = Usuario.objects.filter(is_active=False)
        else:
            usuarios = Usuario.objects.filter(email=a_buscar)
        if usuarios.exists(): # Un método booleano de existencia de objetos
            messages.success(request, 'Usuario(s) encontrado(s).')  # Mensaje de éxito
        else:
            messages.error(request, 'La búsqueda no arrojó resultados.')  # Mensaje de error    
    return render(request, 'administrador_s/buscar_parametros.html', {'usuarios': usuarios})

@login_required
def ver_perfil_administrador_s(request):
    return render(request, 'administrador_s/perfil.html')


@login_required
def activar_usuario(request, usuario_id):
    usuario_activar = get_object_or_404(Usuario, id=usuario_id)
    if usuario_activar == request.user:
        messages.info(request, f"El usuario no tiene permiso para desativar su propia cuenta.")
        return redirect('ver_perfil_administrador_s')
    else:
        usuario_activar.is_active = not usuario_activar.is_active  # Cambia el estado activo/inactivo
        usuario_activar.save()

        estado = "activado" if usuario_activar.is_active else "desactivado" # Condicional python ternario en una sola linea

        messages.info(request, f"El usuario ha sido {estado} correctamente.")

    return redirect('ver_perfil_administrador_s')

#endregion

