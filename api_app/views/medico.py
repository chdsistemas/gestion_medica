from rest_framework import viewsets
from medica_app.models.medico import Medico
from api_app.serializers.medico import MedicoSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


