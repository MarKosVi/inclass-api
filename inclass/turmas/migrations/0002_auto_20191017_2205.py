# Generated by Django 2.2.6 on 2019-10-18 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbhorario_turma_disciplina',
            name='id_horario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turmas.tbhorario'),
        ),
    ]
