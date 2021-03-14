from django.forms import ModelForm, NumberInput, TextInput, Select

from controle_estagios.models import Estagios
from .validacoes import valida_valor


class FormEstagios(ModelForm):

    def clean_valor(self):
        valor = self.cleaned_data['valor']
        return valida_valor(valor)

    class Meta:
        model = Estagios
        fields = '__all__'
        widgets = {
            'valor': NumberInput(attrs={'class': 'form-control', 'value': '0'}),
            'data_inicio': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_prorrogacao': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'aluno': Select(attrs={'class': 'form-control'}),
            'empresa': Select(attrs={'class': 'form-control'}),
        }
