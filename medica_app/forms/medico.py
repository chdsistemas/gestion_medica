from django import forms
from medica_app.models.medico import Medico


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
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
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }