from django.forms import ModelForm, Select, TextInput, EmailInput

from controle_estagios.models import Alunos
from .validacoes import valida_tamanho_string, valida_cep, PAISES, valida_matricula, \
    valida_cpf, valida_tamanho_unico, valida_emails_permitidos, valida_data


class FormAlunos(ModelForm):

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return valida_tamanho_string('NOME', nome, 3, 50)

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

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        return valida_matricula(matricula)

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        return valida_cpf(cpf)

    def clean_celular(self):
        celular = self.cleaned_data['celular']
        return valida_tamanho_unico('CELULAR', celular, 14)

    def clean_email(self):
        email = self.cleaned_data['email']
        return valida_emails_permitidos(email)

    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data['data_nascimento']
        return valida_data(data_nascimento)

    class Meta:
        model = Alunos
        fields = '__all__'
        widgets = {
            'pais': Select(choices=PAISES, attrs={'class': 'form-control'}),
            'nome': TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'}),
            'fone': TextInput(attrs={'class': 'form-control fone-mask', 'placeholder': '(00)0000-0000'}),
            'cep': TextInput(attrs={'class': 'form-control cep-mask', 'placeholder': '00000-000'}),
            'endereco': TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua dos bobos'}),
            'bairro': TextInput(attrs={'class': 'form-control'}),
            'cidade': TextInput(attrs={'class': 'form-control'}),
            'complemento': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nº 0'}),
            'celular': TextInput(attrs={'class': 'form-control celular-mask', 'placeholder': '(00)00000-0000'}),
            'cpf': TextInput(attrs={'class': 'form-control cpf-mask', 'placeholder': '000.000.000-00'}),
            'data_nascimento': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'matricula': TextInput(attrs={'class': 'form-control matricula-mask'}),
            'curso': Select(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'meu_email@dominio.com'}),
        }
