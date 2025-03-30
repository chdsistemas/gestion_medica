from django import forms
from medica_app.models.prestador import Prestador


class PrestadorForm(forms.ModelForm):
    class Meta:
        model = Prestador
        fields = '__all__'
        

        