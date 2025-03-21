"""
URL configuration for gestion_medica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from medica_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),


    path('medico/registrar/', registrar_medico, name='registrar_medico'),
    path('medico/listar/', listar_medicos, name='listar_medicos'),
    path('medico/actualizar/', actualizar_medico, name='actualizar_medico'),
    #path('medico/detallar/<int:medico_id>/', detallar_medico, name='detallar_medico'),
    path('medico/eliminar/<int:medico_id>/', eliminar_medico, name='eliminar_medico'),
    path('medico/ver-perfil/', ver_perfil_medico, name='perfil_medico'),


    path('paciente/registrar/', registrar_paciente, name='registrar_paciente'),
    path('paciente/listar/', listar_pacientes, name='listar_pacientes'),
    path('paciente/actualizar/<int:paciente_id>/', actualizar_paciente, name='actualizar_paciente'),
    path('paciente/detallar/<int:paciente_id>/', detallar_paciente, name='detallar_paciente'),
    path('paciente/eliminar/<int:paciente_id>/', eliminar_paciente, name='eliminar_paciente'),


    path('usuario/registrar/', registrar_usuario, name='registrar_usuario'),
    path('usuario/eliminar/<int:usuario_id>', eliminar_usuario, name='eliminar_usuario'),
    path('usuario-filtro/listar/', listar_usuarios_filtrados, name='listar_usuarios_filtrados'),
    path('usuario/listar/', listar_usuarios, name='listar_usuarios'),
    path('usuario/actualizar/', actualizar_usuario, name='actualizar_usuario'),
    path('usuario/detallar/', detallar_usuario, name='detallar_usuario'),
    path('usuario/ver-perfil/', ver_perfil_usuario, name='perfil_usuario'),
    path('usuario/login/', login_usuario, name='login'),
    path('usuario/logout/', logout_usuario, name='logout'),

    path('cita/registrar/', registrar_cita_medica, name='registrar_cita'),
    path('cita/listar/', listar_citas_medicas, name='listar_citas'),
    path('mis_citas/listar/', listar_mis_citas, name='listar_mis_citas'),
    path('cita/actualizar/<int:paciente_id>/', actualizar_paciente, name='actualizar_paciente'),
    path('cita/detallar/<int:paciente_id>/', detallar_paciente, name='detallar_paciente'),
    path('cita/eliminar/<int:paciente_id>/', eliminar_paciente, name='eliminar_paciente'),

    path('administrador_sistema/registrar/', registrar_administrador_sistema, name='registrar_administrador_s'),
    path('administrador_sistema/listar/', listar_administradores_s, name='listar_administradores_s'),
    path('administrador_sistema/gestionar/', gestionar_usuario, name='gestionar_usuario'),
    path('administrador_sistema/activar/<int:usuario_id>/', activar_usuario, name='activar_usuario'),
    path('administrador_sistema/ver_perfil/', ver_perfil_administrador_s, name='ver_perfil_administrador_s'),
    path('administrador_sistema/buscar_usuario_doc/', buscar_usuario_documento, name='buscar_usuario_documento'),
    path('administrador_sistema/buscar_usuarios_nombre/', buscar_usuarios_nombre, name='buscar_usuarios_nombre'),
    path('administrador_sistema/buscar_general/', usuario_por_parametros, name='buscar_usuarios_parametros'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)