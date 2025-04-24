from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from web_app.models.especialidad import Especialidad
from web_app.forms.especialidad import EspecialidadForm


# Vista basada en clases para crear objetos de Especialidad
class EspecialidadCreateView(CreateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'especialidad/registrar.html'
    success_url = reverse_lazy('listar_especialidades')


# Lista de especialidades médicas
class EspecialidadListView(ListView):
    model = Especialidad
    template_name = 'especialidad/listar.html'
    context_object_name = 'especialidades'


# Actualizar una especialidad médica por su pk
class EspecialidadUpdateView(UpdateView):
    model = Especialidad
    form_class = EspecialidadForm
    template_name = 'especialidad/actualizar.html'
    success_url = reverse_lazy('listar_especialidades')


# Ver los detalles del objeto especialidad
class EspecialidadDetailView(DetailView):
    model = Especialidad
    template_name = 'especialidad/detallar.html'
    context_object_name = 'sede' # Objeto a enviar a 'especialidad/detallar.html'


# Templata de confirmación de eliminación de la especialidad
class EspecialidadDeleteView(DeleteView):
    model = Especialidad
    template_name = 'especialidad/eliminar.html'
    success_url = reverse_lazy('listar_especialidades')

