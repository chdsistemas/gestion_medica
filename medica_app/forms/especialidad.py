from django import forms
from medica_app.models.especialidad import Especialidad


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'


