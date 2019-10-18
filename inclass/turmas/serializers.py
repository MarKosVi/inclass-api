
from rest_framework import serializers
from turmas.models import tbdisciplina
from turmas.models import tbescola
from turmas.models import tbhorario
from turmas.models import tbhorario_turma_disciplina
from turmas.models import tbsala
from turmas.models import tbturma
from turmas.models import tbturma_disciplina
from turmas.models import tbusuario


class TbDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbdisciplina
        fields = '__all__'

class TbEscolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbescola
        fields = '__all__'

class TbHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbhorario
        fields = '__all__'

class TbHorario_Turma_DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbhorario_turma_disciplina
        fields = '__all__'

class TbSalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbsala
        fields = '__all__'

class TbTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbturma
        fields = '__all__'

class TbTurma_DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbturma_disciplina
        fields = '__all__'

class TbUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tbusuario
        fields = '__all__'