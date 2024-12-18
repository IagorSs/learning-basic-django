from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados, PaisViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('aluno', AlunosViewSet, basename='Alunos')
router.register('curso', AlunosViewSet, basename='Cursos')
router.register('matricula', MatriculasViewSet, basename='Matriculas')
router.register('pai', PaisViewSet, basename='Pais')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/alunos/', ListaAlunosMatriculados.as_view())
]
