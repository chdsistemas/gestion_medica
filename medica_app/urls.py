from django.contrib import admin
from django.urls import path
from medica_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
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

    path('adm_sistema/registrar/', registrar_adm_sistema, name='registrar_adm_sistema'),
    path('adm_sistema/listar/', listar_adm_sistema, name='listar_adm_sistema'),
    path('adm_sistema/gestionar/', gestionar_usuario, name='gestionar_usuario'),
    path('adm_sistema/activar/<int:usuario_id>/', activar_usuario, name='activar_usuario'),
    path('adm_sistema/ver_perfil/', ver_perfil_adm_sistema, name='ver_perfil_adm_sistema'),
    path('adm_sistema/buscar_usuario_doc/', buscar_usuario_documento, name='buscar_usuario_documento'),
    path('adm_sistema/buscar_usuarios_nombre/', buscar_usuarios_nombre, name='buscar_usuarios_nombre'),
    path('adm_sistema/buscar_general/', usuario_por_parametros, name='buscar_usuarios_parametros'),

    path('sede/registrar/', SedeCreateView.as_view(), name='registrar_sede'),
    path('sede/listar/', SedeListView.as_view(), name='listar_sedes'),
    path('sede/actualizar/<int:pk>/', SedeUpdateView.as_view(), name='actualizar_sede'),
    path('sede/detallar/<int:pk>/', SedeDetailView.as_view(), name='detallar_sede'),
    path('sede/eliminar/<int:pk>/', SedeDeleteView.as_view(), name='eliminar_sede'),

    path('especialidad/registrar/', EspecialidadCreateView.as_view(), name='registrar_especialidad'),
    path('especialidad/listar/', EspecialidadListView.as_view(), name='listar_especialidades'),
    path('especialidad/actualizar/<int:pk>/', EspecialidadUpdateView.as_view(), name='actualizar_especialidad'),
    path('especialidad/detallar/<int:pk>/', EspecialidadDetailView.as_view(), name='detallar_especialidad'),
    path('especialidad/eliminar/<int:pk>/', EspecialidadDeleteView.as_view(), name='eliminar_especialidad'),    

    path('auxiliar_adm/registrar/', AuxiliarAdministrativoCreateView.as_view(), name='registrar_aux_adm'),
    path('auxiliar_adm/listar/', AuxiliarAdministrativoListView.as_view(), name='listar_aux_adm'),
    path('auxiliar_adm/actualizar/<int:pk>/', AuxiliarAdministrativoUpdateView.as_view(), name='actualizar_aux_adm'),
    path('auxiliar_adm/detallar/<int:pk>/', AuxiliarAdministrativoDetailView.as_view(), name='detallar_aux_adm'),
    path('auxiliar_adm/eliminar/<int:pk>/', AuxiliarAdministrativoDeleteView.as_view(), name='eliminar_aux_adm')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

