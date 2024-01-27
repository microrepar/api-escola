from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno, Curso, Matricula

from .serializer import (AlunoSerializer, CursoSerializer,
                         ListaAlunosMatriculaSerializer,
                         ListaMatriculasAlunoSerializer, MatriculaSerializer)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibi todos os aluno e alunas
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibe todos os curso
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibe todas as matrículas
    """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Lista todas as matriculas de um aluno
    """
    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['id'])
        return queryset
    
    
class ListaAlunosMatricula(generics.ListAPIView):
    """Lista todos os alunos de uma matrícula
    """
    serializer_class = ListaAlunosMatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]    

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['id'])
        return queryset