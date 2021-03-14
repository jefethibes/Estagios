# Generated by Django 3.1.6 on 2021-02-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estagios', '0002_auto_20210208_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='matricula',
            field=models.IntegerField(max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='cnpj',
            field=models.CharField(max_length=18),
        ),
    ]
