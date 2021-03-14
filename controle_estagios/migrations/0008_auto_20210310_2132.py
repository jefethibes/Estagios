# Generated by Django 3.1.6 on 2021-03-11 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle_estagios', '0007_auto_20210308_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='unidades',
        ),
        migrations.AddField(
            model_name='cursos',
            name='instituicao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='controle_estagios.instituicao'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Unidades',
        ),
    ]