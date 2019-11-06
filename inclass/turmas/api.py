from turmas.models import tbdisciplina
from turmas.models import tbescola
from turmas.models import tbhorario 
from turmas.models import tbhorario_turma_disciplina 
from turmas.models import tbsala 
from turmas.models import tbturma 
from turmas.models import tbturma_disciplina 
from turmas.models import tbusuario 
from rest_framework import viewsets, permissions
from .serializers import TbDisciplinaSerializer
from .serializers import TbEscolaSerializer
from .serializers import TbHorarioSerializer
from .serializers import TbHorario_Turma_DisciplinaSerializer
from .serializers import TbSalaSerializer
from .serializers import TbTurmaSerializer
from .serializers import TbTurma_DisciplinaSerializer
from .serializers import TbUsuarioSerializer
#from .serializer import SouverSerializer

#Class SouverView
# class SouverViewSet()

class TbDisciplinaViewSet(viewsets.ModelViewSet):
    queryset = tbdisciplina.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbDisciplinaSerializer


class TbEscolaViewSet(viewsets.ModelViewSet):
    queryset = tbescola.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbEscolaSerializer

class TbHorarioViewSet(viewsets.ModelViewSet):
    queryset = tbhorario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbHorarioSerializer

class TbHorario_Turma_DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = tbhorario_turma_disciplina.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbHorario_Turma_DisciplinaSerializer

class TbSalaViewSet(viewsets.ModelViewSet):
    queryset = tbsala.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbSalaSerializer

class TbTurmaViewSet(viewsets.ModelViewSet):
    queryset = tbturma.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbTurmaSerializer

class TbTurma_DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = tbturma_disciplina.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbTurma_DisciplinaSerializer

class TbUsuarioViewSet(viewsets.ModelViewSet):
    queryset = tbusuario.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TbUsuarioSerializer
