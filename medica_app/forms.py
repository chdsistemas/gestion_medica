from django import forms
from medica_app.models import *
from django.core.exceptions import ValidationError
import os


class FormularioUsuario(forms.ModelForm):
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



class FormularioMedico(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'tipo_doc',
            'num_doc',
            'numero_carnet',
            'username', # Atributo del modelo Usuario
            'first_name', 
            'last_name',
            'ciudad_res',
            'direccion',
            'telefono',
            'especialidad',
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
     
        

class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'tipo_doc',
            'num_doc',
            'username', # Atributo del modelo Usuario
            'first_name', 
            'last_name',
            'ciudad_res',
            'direccion',
            'telefono',
            'fecha_nac',
            'email',
            'password',
            'tipo',
            'genero',            
            'imagen',
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }


class FormularioAuxiliarEnfermeria(forms.ModelForm):
    class Meta:
        model = AuxiliarEnfermeria
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
            'departamento',        
            'imagen'
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }



class FormularioAdministradorSistema(forms.ModelForm):
    class Meta:
        model = AdministradorSistema
        fields = [
            'tipo_doc',    
            'num_doc',
            'codigo',         
            'username', # Atributo del modelo Usuario
            'first_name', 
            'last_name',
            'profesion',
            'ciudad_res',
            'direccion',
            'telefono',
            'fecha_nac',
            'fecha_ingreso',
            'email',
            'password',           
            'imagen',
            'rol'
            ]
        widgets = {
            'password': forms.PasswordInput(),
            'fecha_nac': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ingreso':forms.DateInput(attrs={'type': 'date'}),
            'imagen': forms.FileInput()
        }



class FormularioCitaMedica(forms.ModelForm):
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


