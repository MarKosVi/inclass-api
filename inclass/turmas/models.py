from django.db import models



class tbdisciplina(models.Model):
    nome = models.CharField(max_length=100)
    tipo_sala = models.BinaryField(1)
    id_escola = models.CharField(max_length=45)
    created_date = models.DateTimeField(auto_now_add=True)

class tbescola(models.Model):
    nome = models.CharField(max_length=45, blank=False)
    id_usuario = models.IntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)


class tbhorario(models.Model):
    dia_semana = models.CharField(max_length=45)
    horario = models.CharField(max_length=45)

class tbhorario_turma_disciplina(models.Model):
    id_horario = models.ForeignKey(tbhorario, on_delete=models.PROTECT)
    id_disciplina = models.IntegerField(11, null=False)
    id_sala = models.IntegerField(11, null=False)

class tbsala(models.Model):
    campus = models.CharField(max_length=45)
    capacidade = models.IntegerField(11, null=False)
    localizacao = models.IntegerField(11, null=False)
    tipo = models.BinaryField(1)

class tbturma(models.Model):
    qtd_alunos = models.IntegerField(11)
    cod_turma = models.CharField(max_length=45, null=False)
    curso = models.CharField(max_length=45)
    turno = models.CharField(max_length=45)
    id_escola = models.IntegerField(11, null=False)

class tbturma_disciplina(models.Model):
    id_turma = models.IntegerField(11, null=False)
    id_disciplina = models.IntegerField(11, null=False)
    ano = models.IntegerField(11, null=False)
    semestre = models.IntegerField(11, null=False)

class tbusuario(models.Model):
    login = models.CharField(max_length=45)
    senha = models.CharField(max_length=45)
    id_escola = models.IntegerField(11, null=False)