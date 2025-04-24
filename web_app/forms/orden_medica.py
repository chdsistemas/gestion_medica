from django import forms
from web_app.models.orden_medica import OrdenMedica


class OrdenForm(forms.ModelForm):
    class Meta:
        model = OrdenMedica
        fields = '__all__'
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }