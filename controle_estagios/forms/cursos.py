from django.forms import ModelForm, TextInput

from controle_estagios.models import Cursos
from .validacoes import valida_tamanho_string


class FormCursos(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return valida_tamanho_string('NOME', nome, 3, 150)

    class Meta:
        model = Cursos
        fields = '__all__'
        widgets = {
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
        }
