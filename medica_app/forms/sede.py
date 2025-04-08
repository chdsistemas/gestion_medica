from django import forms
from medica_app.models.sede import Sede


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ['codigo', 'nombre', 'descripcion']
