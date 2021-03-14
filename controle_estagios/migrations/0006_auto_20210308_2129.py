# Generated by Django 3.1.6 on 2021-03-09 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estagios', '0005_auto_20210227_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='matricula',
            field=models.IntegerField(unique=True),
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='unidades',
        ),
        migrations.AddField(
            model_name='cursos',
            name='unidades',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='controle_estagios.unidades'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='cnpj',
            field=models.CharField(max_length=18, unique=True),
        ),
    ]
