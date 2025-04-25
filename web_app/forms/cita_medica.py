from django import forms
from web_app.models.cita_medica import CitaMedica


class CitaMedicaForm(forms.ModelForm):
    class Meta:
        model = CitaMedica
        fields = [
            'sede',
            'consultorio',
            'fecha',
            'hora',
            'sede',
            'medico',
            'paciente'
            ]
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'})
        }

