from django import forms
from web_app.models.agenda_medica import AgendaMedica


class AgendaForm(forms.ModelForm):
    class Meta:
        model = AgendaMedica
        fields = '__all__'
        

        