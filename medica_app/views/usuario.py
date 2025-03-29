from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from medica_app.models.usuario import Usuario
from medica_app.forms.usuario import UsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
                return render(request, 'adm_sistema/perfil.html', {'tipo_usuario': 'Administrador de Sistema'})
            else:
                return render(request, 'usuario/perfil.html', {'tipo_usuario': 'Usuario sin rol en el sistema'})
        return render(request, 'usuario/login.html', {'mensaje_error': 'Credenciales incorrectas, intente de nuevo o consulte con Administrador de Sistema'})
    return render(request, 'usuario/login.html')


def logout_usuario(request):
    logout(request)
    return redirect('home')


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, request.FILES)
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
        formulario = UsuarioForm()
    return render(request, 'usuario/insertar.html', {'formulario': formulario})



@login_required
def actualizar_usuario(request):
    usuario = request.user  # Usuario logueado
    if request.method == 'POST':
        formulario = UsuarioForm(request.POST, request.FILES, instance=usuario)  # Se incluye request.FILES
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
        formulario = UsuarioForm(instance=usuario)
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