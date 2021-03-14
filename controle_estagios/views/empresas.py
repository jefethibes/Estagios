from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from controle_estagios.forms.empresas import FormEmpresas
from controle_estagios.models import Empresas


class AddEmpresas(SuccessMessageMixin, CreateView):
    form_class = FormEmpresas
    template_name = 'controle_estagios/empresas/form_empresas.html'
    success_url = reverse_lazy('controle_estagios:list_empresas')
    success_message = 'Empresa cadastrada com sucesso!'


class ListEmpresas(ListView):
    form = FormEmpresas
    template_name = 'controle_estagios/empresas/list_empresas.html'
    paginate_by = 10

    def get_queryset(self):
        return Empresas.objects.all()


class UpdateEmpresas(SuccessMessageMixin, UpdateView):
    model = Empresas
    form_class = FormEmpresas
    template_name = 'controle_estagios/empresas/form_empresas.html'
    success_url = reverse_lazy('controle_estagios:list_empresas')
    success_message = 'Empresa alterada com sucesso!'
