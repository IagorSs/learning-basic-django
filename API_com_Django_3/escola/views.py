from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula, Pai
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer, PaiSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os alunos e alunas"""
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
  """Exibindo todos os cursos"""
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class PaisViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Pais"""
  queryset = Pai.objects.all()
  serializer_class = PaiSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
  """Exibindo todos os Matriculas"""
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
  """Listando as matriculas de um aluno"""
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno=self.kwargs['pk'])
    return queryset

  serializer_class = ListaMatriculasAlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
  """Listando alunos matriculados em um curso"""
  def get_queryset(self):
    return Matricula.objects.filter(curso=self.kwargs['pk'])

  serializer_class = ListaAlunosMatriculadosSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]