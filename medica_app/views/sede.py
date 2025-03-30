from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from medica_app.models.sede import Sede
from medica_app.forms.sede import SedeForm


class SedeCreateView(CreateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sede/registrar.html'
    success_url = reverse_lazy('listar_sedes')


#@login_required
class SedeListView(ListView):
    model = Sede
    template_name = 'sede/listar.html'
    context_object_name = 'sedes' # Variable que se pasará al archivo listar.html


#@login_required
class SedeUpdateView(UpdateView):
    model = Sede
    form_class = SedeForm
    template_name = 'sede/actualizar.html'
    success_url = reverse_lazy('listar_sedes')


#@login_required
class SedeDetailView(DetailView):
    model = Sede
    template_name = 'sede/detallar.html'
    context_object_name = 'sede' # Objeto a enviar al detalle.html


#@login_required
class SedeDeleteView(DeleteView):
    model = Sede
    template_name = 'sede/eliminar.html'
    success_url = reverse_lazy('listar_sedes')
