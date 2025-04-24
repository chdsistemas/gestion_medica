from django import forms
from web_app.models.consultorio import Consultorio


class ConsultorioForm(forms.ModelForm):
    class Meta:
        model = Consultorio
        fields = '__all__'
