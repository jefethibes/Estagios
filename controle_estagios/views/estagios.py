from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from controle_estagios.forms.estagios import FormEstagios
from controle_estagios.models import Estagios


class AddEstagios(SuccessMessageMixin, CreateView):
    form_class = FormEstagios
    template_name = 'controle_estagios/estagios/form_estagios.html'
    success_url = reverse_lazy('controle_estagios:list_estagios')
    success_message = 'Estágio cadastrado com sucesso!'


class ListEstagios(ListView):
    form = FormEstagios
    template_name = 'controle_estagios/estagios/list_estagios.html'
    paginate_by = 10

    def get_queryset(self):
        return Estagios.objects.all()


class UpdateEstagios(SuccessMessageMixin, UpdateView):
    model = Estagios
    form_class = FormEstagios
    template_name = 'controle_estagios/estagios/form_estagios.html'
    success_url = reverse_lazy('controle_estagios:list_estagios')
    success_message = 'Estágio alterado com sucesso!'
