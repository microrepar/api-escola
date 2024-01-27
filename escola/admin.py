from django.contrib import admin

from .models import Aluno, Curso, Matricula

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20


class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo', 'descricao')
    search_fields = ('descricao', )
    list_per_page = 20


class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id', 'curso', 'periodo')


admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Matricula, MatriculaAdmin)
