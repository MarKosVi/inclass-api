# Generated by Django 2.2.6 on 2019-10-18 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbdisciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo_sala', models.BinaryField(verbose_name=1)),
                ('id_escola', models.CharField(max_length=45)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbescola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=45)),
                ('id_usuario', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbhorario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=45)),
                ('horario', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='tbhorario_turma_disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_horario', models.IntegerField(verbose_name=11)),
                ('id_disciplina', models.IntegerField(verbose_name=11)),
                ('id_sala', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.CreateModel(
            name='tbsala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campus', models.CharField(max_length=45)),
                ('capacidade', models.IntegerField(verbose_name=11)),
                ('localizacao', models.IntegerField(verbose_name=11)),
                ('tipo', models.BinaryField(verbose_name=1)),
            ],
        ),
        migrations.CreateModel(
            name='tbturma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qtd_alunos', models.IntegerField(verbose_name=11)),
                ('cod_turma', models.CharField(max_length=45)),
                ('curso', models.CharField(max_length=45)),
                ('turno', models.CharField(max_length=45)),
                ('id_escola', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.CreateModel(
            name='tbturma_disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_turma', models.IntegerField(verbose_name=11)),
                ('id_disciplina', models.IntegerField(verbose_name=11)),
                ('ano', models.IntegerField(verbose_name=11)),
                ('semestre', models.IntegerField(verbose_name=11)),
            ],
        ),
        migrations.CreateModel(
            name='tbusuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=45)),
                ('senha', models.CharField(max_length=45)),
                ('id_escola', models.IntegerField(verbose_name=11)),
            ],
        ),
    ]