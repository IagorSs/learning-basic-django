from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula, Pai


class AlunoSerializer(serializers.ModelSerializer):
    pai = serializers.ReadOnlyField(source='pai.nome')

    class Meta:
        model = Aluno
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')

    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source='aluno.nome')

    class Meta:
        model = Matricula
        fields = ['aluno']

class PaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pai
        fields = '__all__'
