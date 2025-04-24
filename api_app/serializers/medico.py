from rest_framework import serializers
from web_app.models.medico import Medico


class MedicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Medico
        fields = [
            'id',
            'tipo_doc',
            'num_doc',
            'numero_carnet',
            'username',
            'first_name', 
            'last_name',
            'ciudad_res',
            'direccion',
            'telefono',
            'especialidad',
            'fecha_nac',
            'email',
            'password',
            'imagen'
            ]
        
        