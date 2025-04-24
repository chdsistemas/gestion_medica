from django import forms
from web_app.models.aux_administrativo import AuxiliarAdministrativo


class AuxiliarAdministrativoForm(forms.ModelForm):
    class Meta:
        model = AuxiliarAdministrativo
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
            'imagen'
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ing': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }