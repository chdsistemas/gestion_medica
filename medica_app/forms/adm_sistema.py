from django import forms
from medica_app.models.adm_sistema import AdministradorSistema


class AdministradorSistemaForm(forms.ModelForm):
    class Meta:
        model = AdministradorSistema
        fields = [
            'tipo_doc',    
            'num_doc',
            'codigo',         
            'username',
            'first_name', 
            'last_name',
            'profesion',
            'ciudad_res',
            'direccion',
            'telefono',
            'fecha_nac',
            'fecha_ingreso',
            'email', 
            'acciones',         
            'imagen',
            'password'
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ingreso':forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }