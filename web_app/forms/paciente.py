from django import forms
from web_app.models.paciente import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
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
            'tipo',
            'genero',            
            'imagen',
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }