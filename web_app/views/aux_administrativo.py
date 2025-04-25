from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from web_app.models.aux_administrativo import AuxiliarAdministrativo
from web_app.forms.auxiliar_adm import AuxiliarAdministrativoForm


# Vista basada en clases para crear objetos de Auxiliar Administrativo
class AuxiliarAdministrativoCreateView(CreateView):
    model = AuxiliarAdministrativo
    form_class = AuxiliarAdministrativoForm
    template_name = 'auxiliar_adm/registrar.html'
    success_url = reverse_lazy('listar_aux_adm')

    def form_valid(self, form):
        # Cifra la contraseña antes de guardar el auxiliar
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # importante
        user.save()
        return super().form_valid(form)


# Lista de auxiliares administrativos
class AuxiliarAdministrativoListView(ListView):
    model = AuxiliarAdministrativo
    template_name = 'auxiliar_adm/listar.html'
    context_object_name = 'aux_adm' # Variable que se pasará al archivo listar.html


# Actualizar un aux adm por su pk
class AuxiliarAdministrativoUpdateView(UpdateView):
    model = AuxiliarAdministrativo
    form_class = AuxiliarAdministrativoForm
    template_name = 'auxiliar_adm/actualizar.html'
    success_url = reverse_lazy('listar_aux_adm')


class AuxiliarAdministrativoDetailView(DetailView):
    model = AuxiliarAdministrativo
    template_name = 'auxiliar_adm/detallar.html'
    context_object_name = 'aux_adm' # Objeto a enviar al detalle.html


class AuxiliarAdministrativoDeleteView(DeleteView):
    model = AuxiliarAdministrativo
    template_name = 'auxiliar_adm/eliminar.html'
    success_url = reverse_lazy('listar_aux_adm')
