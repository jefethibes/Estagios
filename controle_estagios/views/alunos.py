from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from controle_estagios.forms.alunos import FormAlunos
from controle_estagios.models import Alunos


class AddAlunos(SuccessMessageMixin, CreateView):
    form_class = FormAlunos
    template_name = 'controle_estagios/alunos/form_alunos.html'
    success_url = reverse_lazy('controle_estagios:list_alunos')
    success_message = 'Aluno cadastrado com sucesso!'


class ListAlunos(ListView):
    form = FormAlunos
    template_name = 'controle_estagios/alunos/list_alunos.html'
    paginate_by = 10

    def get_queryset(self):
        return Alunos.objects.all()


class UpdateAlunos(SuccessMessageMixin, UpdateView):
    model = Alunos
    form_class = FormAlunos
    template_name = 'controle_estagios/alunos/form_alunos.html'
    success_url = reverse_lazy('controle_estagios:list_alunos')
    success_message = 'Aluno alterado com sucesso!'
