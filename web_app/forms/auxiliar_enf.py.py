from django import forms
from web_app.models.auxiliar_enf import AuxiliarEnfermeria


class AuxiliarEnfermeriaForm(forms.ModelForm):
    class Meta:
        model = AuxiliarEnfermeria
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
            'departamento',        
            'imagen'
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }