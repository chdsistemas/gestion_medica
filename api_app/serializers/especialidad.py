from rest_framework import serializers
from medica_app.models.especialidad import Especialidad


class EspecialidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Especialidad
        fields = '__all__'

        