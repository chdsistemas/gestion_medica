from django import forms
from medica_app.models.usuario import Usuario
from django.core.exceptions import ValidationError
import os


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'tipo_doc',
            'num_doc',
            'username',
            'first_name', 
            'last_name',
            'ciudad_res',
            'direccion',
            'telefono',
            'fecha_nac',
            'email',
            'password',
            'imagen'
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }

    def validar_imagen(self):
        imagen = self.cleaned_data.get(imagen)

        if imagen:
            extension = os.path.splitext(imagen.name)[1].lower() #Verifica la extensión del archivo
            if extension not in ['jpg', 'png', 'jpeg']:
                raise ValidationError('Debe anexar solo archivos gráficos PNG/JPG/JPEG')
            
            if imagen.size > 102400:
                raise ValidationError('El tamaño máximo del archivo es 100 KB')
        return imagen