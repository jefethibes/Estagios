# Generated by Django 3.1.6 on 2021-03-09 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estagios', '0006_auto_20210308_2129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='unidades',
        ),
        migrations.AddField(
            model_name='cursos',
            name='unidades',
            field=models.ManyToManyField(to='controle_estagios.Unidades'),
        ),
    ]
