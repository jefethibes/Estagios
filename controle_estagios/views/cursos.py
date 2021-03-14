from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from controle_estagios.forms.cursos import FormCursos
from controle_estagios.models import Cursos


class AddCursos(SuccessMessageMixin, CreateView):
    form_class = FormCursos
    template_name = 'controle_estagios/cursos/form_cursos.html'
    success_url = reverse_lazy('controle_estagios:list_cursos')
    success_message = 'Curso cadastrado com sucesso!'


class ListCursos(ListView):
    form = FormCursos
    template_name = 'controle_estagios/cursos/list_cursos.html'
    paginate_by = 10

    def get_queryset(self):
        return Cursos.objects.all()


class UpdateCursos(SuccessMessageMixin, UpdateView):
    model = Cursos
    form_class = FormCursos
    template_name = 'controle_estagios/cursos/form_cursos.html'
    success_url = reverse_lazy('controle_estagios:list_cursos')
    success_message = 'Curso alterado com sucesso!'
