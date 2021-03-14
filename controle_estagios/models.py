from django.db import models


class Endereco(models.Model):
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=150)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)
    fone = models.CharField(max_length=13, blank=True, null=True)


class Cursos(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Alunos(Endereco):
    nome = models.CharField(max_length=150)
    matricula = models.IntegerField(unique=True)
    data_nascimento = models.DateField(default=True)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField()
    celular = models.CharField(max_length=14)
    curso = models.ForeignKey(Cursos, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Empresas(Endereco):
    nome = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome


class Estagios(models.Model):
    valor = models.FloatField()
    data_inicio = models.DateField()
    data_fim = models.DateField()
    data_prorrogacao = models.DateField(blank=True, null=True)
    aluno = models.ForeignKey(Alunos, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)
