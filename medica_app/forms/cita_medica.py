from django import forms
from medica_app.models.cita_medica import CitaMedica


class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = [
            'codigo',
            'ciudad',
            'direccion',
            'paciente',
            'medico',
            'fecha',
            'hora',
            'consultorio'
            ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
        