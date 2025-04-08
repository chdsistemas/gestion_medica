from rest_framework import viewsets
from medica_app.models.medico import Medico
from api_app.serializers.medico import MedicoSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    """
    API para procesar Medico.

    list:
    Lista todos los medicos.

    create:
    Crea un nuevo médico.

    retrieve:
    Muestra un médico basado en su ID.

    update:
    Actualiza todos los campos de un médico.

    partial_update:
    Actualiza uno o más propiedades de un médico.

    destroy:
    Elimina un médico.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
