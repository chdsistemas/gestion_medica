from django import forms
from medica_app.models.autorizacion import Autorizacion


class AutorizacionForm(forms.ModelForm):
    class Meta:
        model = Autorizacion
        fields = '__all__'
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }
        