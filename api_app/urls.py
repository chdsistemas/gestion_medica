from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app.views.medico import MedicoViewSet
from api_app.views.paciente import PacienteViewSet
from api_app.views.especialidad import EspecialidadViewSet
 
# Codificar rutas de APIs

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet, basename='medico')
router.register(r'pacientes', PacienteViewSet, basename='paciente')
router.register(r'especialidades', EspecialidadViewSet, basename='especialidad')

urlpatterns = [
    path('', include(router.urls)) # Agregar las rutas generadas por la clase router
]

