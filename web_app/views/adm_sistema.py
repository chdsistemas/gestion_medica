from web_app.forms.adm_sistema import AdministradorSistemaForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from web_app.models import AdministradorSistema
from web_app.models import Usuario
from django.contrib.auth.decorators import login_required



def registrar_adm_sistema(request):
    if request.method == 'POST':
        formulario = AdministradorSistemaForm(request.POST, request.FILES)
        if formulario.is_valid():
            administrador_s = formulario.save(commit=False) # Solo guardar el objeto en memoria, más tarde se guarda en la bd
            # Cifra la contraseña utilizando set_password()
            #administrador_s.set_password(formulario.cleaned_data['password'])
            administrador_s.save()
            messages.success(request, 'Administrador de sistema creado exitosamente.')
            return redirect('registrar_adm_sistema')
        else:
            messages.error(request, 'Hay algunos errores en el registro. Vuelva a intentar...')
    else:
        formulario = AdministradorSistemaForm()
    return render(request, 'adm_sistema/insertar.html', {'formulario': formulario})


@login_required
def listar_adm_sistema(request):
    administradores_s = AdministradorSistema.objects.all()
    return render(request, 'adm_sistema/listar.html', {'administradores_s': administradores_s})


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
    return render(request, 'adm_sistema/gestionar_usuario.html', {'usuario': usuario})


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
    return render(request, 'adm_sistema/buscar_documento.html', {'usuario': usuario})


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
    return render(request, 'adm_sistema/buscar_nombre.html', {'usuarios': usuarios})


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
    return render(request, 'adm_sistema/buscar_parametros.html', {'usuarios': usuarios})

@login_required
def ver_perfil_adm_sistema(request):
    return render(request, 'adm_sistema/perfil.html')


@login_required
def activar_usuario(request, usuario_id):
    usuario_activar = get_object_or_404(Usuario, id=usuario_id)
    if usuario_activar == request.user:
        messages.info(request, f"El usuario no tiene permiso para desactivar su propia cuenta.")
        return redirect('ver_perfil_adm_sistema')
    else:
        usuario_activar.is_active = not usuario_activar.is_active  # Cambia el estado activo/inactivo
        usuario_activar.save()

        estado = "activado" if usuario_activar.is_active else "desactivado" # Condicional python ternario en una sola linea

        messages.info(request, f"El usuario ha sido {estado} correctamente.")

    return redirect('ver_perfil_adm_sistema')
