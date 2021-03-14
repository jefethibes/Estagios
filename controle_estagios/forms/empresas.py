from django.forms import ModelForm, Select, TextInput

from controle_estagios.models import Empresas
from .validacoes import valida_tamanho_string, valida_cnpj, valida_cep, PAISES


class FormEmpresas(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return valida_tamanho_string('NOME', nome, 3, 150)

    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        return valida_cnpj(cnpj)

    def clean_cep(self):
        cep = self.cleaned_data['cep']
        return valida_cep(cep)

    def clean_endereco(self):
        endereco = self.cleaned_data['endereco']
        return valida_tamanho_string('ENDEREÇO', endereco, 3, 150)

    def clean_bairro(self):
        bairro = self.cleaned_data['bairro']
        return valida_tamanho_string('BAIRRO', bairro, 3, 50)

    def clean_cidade(self):
        cidade = self.cleaned_data['cidade']
        return valida_tamanho_string('CIDADE', cidade, 3, 30)

    def clean_fone(self):
        fone = self.cleaned_data['fone']
        return valida_tamanho_string('TELEFONE', fone, 0, 13)

    class Meta:
        model = Empresas
        fields = '__all__'
        widgets = {
            'pais': Select(choices=PAISES, attrs={'class': 'form-control'}),
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'}),
            'cnpj': TextInput(attrs={'class': 'form-control cnpj-mask', 'placeholder': '00.000.000/0001-00'}),
            'fone': TextInput(attrs={'class': 'form-control fone-mask', 'placeholder': '(00)0000-0000'}),
            'cep': TextInput(attrs={'class': 'form-control cep-mask', 'placeholder': '00000-000'}),
            'endereco': TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua dos bobos'}),
            'bairro': TextInput(attrs={'class': 'form-control'}),
            'cidade': TextInput(attrs={'class': 'form-control'}),
            'complemento': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nº 0'})
        }
