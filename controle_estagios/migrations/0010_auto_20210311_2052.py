# Generated by Django 3.1.6 on 2021-03-11 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estagios', '0009_auto_20210310_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='celular',
            field=models.CharField(max_length=14),
        ),
    ]
