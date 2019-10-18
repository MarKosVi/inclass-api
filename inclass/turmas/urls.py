from rest_framework import routers
from .api import TbDisciplinaViewSet
from .api import TbEscolaViewSet
from .api import TbHorarioViewSet
from .api import TbHorario_Turma_DisciplinaViewSet
from .api import TbSalaViewSet
from .api import TbTurmaViewSet
from .api import TbTurma_DisciplinaViewSet
from .api import TbUsuarioViewSet

router = routers.DefaultRouter()
router.register('disciplina', TbDisciplinaViewSet, 'turmas')
router.register('escola', TbEscolaViewSet, 'turmas')
router.register('horario', TbHorarioViewSet, 'turmas')
router.register('horario_turma_disciplina', TbHorario_Turma_DisciplinaViewSet, 'turmas')
router.register('sala', TbSalaViewSet, 'turmas')
router.register('turma', TbTurmaViewSet, 'turmas')
router.register('turma_disciplina', TbTurma_DisciplinaViewSet, 'turmas')
router.register('usuario', TbUsuarioViewSet, 'turmas')

urlpatterns = router.urls