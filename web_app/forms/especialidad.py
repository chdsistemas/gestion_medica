from django import forms
from web_app.models.especialidad import Especialidad


class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'


