from rest_framework import viewsets
from web_app.models.medico import Medico
from api_app.serializers.medico import MedicoSerializer


class MedicoViewSet(viewsets.ModelViewSet):
    
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
