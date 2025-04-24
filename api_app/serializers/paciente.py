from rest_framework import serializers
from web_app.models.paciente import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Paciente
        fields = [
            'id',
            'tipo_doc',
            'num_doc',
            'username',
            'first_name', 
            'last_name',
            'ciudad_res',
            'direccion',
            'telefono',
            'fecha_nac',
            'email',
            'password',        
            'imagen'
            ]