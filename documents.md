Conteúdo do 1 ao 8:
    Criamos uma pasta para manter todo código da nossa aplicação;
    Utilizamos o módulo venv, que fornece suporte para a criação de ambientes virtuais leves com seus próprios diretórios, opcionalmente isolados dos diretórios do sistema;
    Utilizamos o pip para instalar o Django em nosso ambiente virtual;
    Iniciamos o desenvolvimento da nossa aplicação com o comando django-admin start project alurareceita e subimos o servidor com o comando python manage.py runserver.
1. Criar o diretório do projeto

2. Abrir o diretório com o vscode

3. Criar o ambiente virtual python para o projeto
    Algumas estratégias:
        -1 Venv (biblioteca padrão)
        -2 Virtualenv (necessita importação)
        -3 Virtualenvwrapper-win

4. Instalação das dependências:
    - Django>=3.0,<4.0

5. > django-admin help
        [django]
            - [check, compilemessages, createcachetable, dbshell, diffsettings, 
              dumpdata, flush, inspectdb, loaddata, makemessages, makemigrations, 
              migrate, runserver, sendtestemail, shell, showmigrations, sqlflush, sqlmigrate, 
              sqlsequencereset, squashmigrations, startapp, startproject, test]
    
    5.1. Criação do projeto django:
        > django-admin startproject [nome_do_projeto] . (cria o projeto django a partir do diretório corrente)

    5.2 Definir idioma padrão e o timezone: 
            ```
            from pytz import country_names, country_timezones
            all_timezones = [country_timezones.get(country) for country in country_names]
            all_timezones
            ```
        - LANGUAGE_CODE = 'pt-br'
        - TIME-ZONE =   (pesquisar pelo termo "django timezone list")
    
6. Subir o server da aplicação localmente
    > python manage.py help (comando para listar os parâmetros que pode ser utilizados)
        [auth]
            changepassword
            createsuperuser

        [contenttypes]
            remove_stale_contenttypes

        [django]
            [check, compilemessages, createcachetable, dbshell, diffsettings, dumpdata, 
            flush, inspectdb, loaddata, makemessages, makemigrations, migrate, sendtestemail, 
            shell, showmigrations, sqlflush, sqlmigrate, sqlsequencereset, squashmigrations, 
            startapp, startproject, test, testserver] 
        
        [sessions]
            clearsessions

        [staticfiles]
            collectstatic
            findstatic
            runserver

    6.1. > python manage.py runserver

7. Criar novo app django
    > python manage.py startapp [nome_do_app]

8. Registrar o novo app criado
    - Adicionar o novo app em settings.py
    - Criar no diretório do novo app o arquivo urls.py
    - Definir as rotas do novo app no arquivo urls.py
    - Definir as views que serão utilizadas nas rotas.
    - Incluir as rotas definas do app no arquivo urls.py do setup

9. Vamos isolar nosso html, criar a pasta de templates, carregar as imagens, css e javascript da página, deixando o site com uma aparência bem agradável!
    -Implementar os templates a serem utilizado pelas views
        a. criar diretório com o nome templates dentro do app criado
        b. adicionar um novo arquivo com extensão html no diretório templates
        c. implementar a pagina html que será renderizada pela view do app
        d. adicionar o nome do arquivo html à view para ser renderizada pela aplicação

10. Gerenciando arquivos estáticos no django
    - Alterar o settings.py
        a. adicionar o caminho do diretório templates na chave 'DIRS' do dicionário contido na lista da variável TEMPLATES:
            - {... 'DIRS': [os.path.join(BASE_DIR, 'receitas/templates')], ...}
        b. especificar para o django onde serão encontrados os arquivos staticos para os templates definidos com as seguintes variáveis em settings.py:
            - STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        c. criar um diretório com o nome static no diretório de setup da aplicação
            - Adicionar a seguinte variável em settings.py: STATICFILES_DIRS = [os.path.join(BASE_DIR, 'setup/static')]
        d. adicionar os arquivos estáticos no novo diretório criado no setup da aplicação
        e. executar o comando de coleta dos arquivos estáticos pela aplicação.
            > python manage.py collectstatic

11. Adicionar as tag_templates de referência dos arquivos estáticos nos templates html.
    tags utilizadas:
        - {% load static %}
        - {% block nome_do_bloco %}{% endblock nome_do_bloco %}
        - {% url "nome_da_view" %}
        - {% static "endereco_do_recurso" %}
        - {% include "partials/nome_partial.html" %}
    
12. Ajustar os links do site e melhorar o código dos templates criando partials e evitar código duplicado!
    tags utilizadas:
        - {% load static %}
        - {% include "partials/nome_partial.html" %}

13. Implementação dos templates com as tags.
    {% for chave, valor in dicionario.item %}
        {{ valor }}
    {% endfor %}

14. Instalar dependências do banco de dados e configurar os dados de conexão em settings.py
    - psycopg2, psycopg2-binary
    ```
        DATABASES = {
            'default': {
                'ENGINE'   : 'django.db.backends.postgresql',
                'NAME'     : 'nome_do_banco_de_dados',
                'USER'     : 'user_name',
                'PASSWORD' : 'senha',
                'HOST'     : 'localhost',
            }
        }
    ```

15. Definir as classes de domínio da aplicação mapeando elas para o modelo do Django ORM.
    - Criar diretório para os modelos com o nome models/
    - adicionar arquivos __init__.py com a importação dos modulos model.py

16. Criar a migração com o comando ´python manage.py makemigrations´ (arquivos que definem toda a estrutura DDL do banco de dados por meio do ORM).

17. Executar os scripts de migração para a criação do banco de dados da aplicação.
    > python manage.py migrate

18. Criar um superuser com o comando ´python manage.py createsuperuser´ para gerenciamento administrativo da aplicação.

19. Registrar os modelos no módulo admin do app para serem gerenciados pela interface admin do django.
    - adicionar arquivos __init__.py com a importação dos modulos admin.py
    - admin.site.register(NomeDaClasse, AdminModel)

20. Configurar o modulo admin para customização da interface
    Ex.:
        from django.contrib import admin
        from .models import Receita

        class ListandoReceitas(admin.ModelAdmin):
            list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
            list_display_links = ('id', 'nome_receita',)
            search_fields = ('nome_receita', )
            list_filter = ('categoria',)
            list_editable = ('publicada',)
            list_per_page = 2

        admin.site.register(Receita, ListandoReceitas)

21. Removendo um app django.
    - Retirar o registro da lista "INSTALLED_APPS"
    - Retirar as referências do app dos outros apps que serão mantivos
    - Corrigir as migrations que tem dependem do app removido
    - Remover todos os imports do app removido dos apps que a utilizavam.
    - Apagar a base de dados e realizar nova migração.


############################### DJANGO REST FRAMEWORK ###############################
1. Instalar o djangorestframework e markdown
    - pip install djangorestframework
    - pip install markdown
    
2. Implementar os Serializers
    ```
    from rest_framework import serializers
    from escola.models import Aluno, Curso, Matricula

    class AlunoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Aluno
            fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


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


    class ListaAlunosMatriculaSerializer(serializers.ModelSerializer):
        nome_aluno = serializers.ReadOnlyField(source='aluno.nome')
        curso = serializers.ReadOnlyField(source='curso.descricao')
        periodo = serializers.SerializerMethodField()

        class Meta:
            model = Matricula
            fields = ['nome_aluno', 'curso', 'periodo']

        def get_aluno(self, obj):
            return obj.get_nome_display()
        
        def get_periodo(self, obj):
            return obj.get_periodo_display()
        
    ```

3. Implementar as ViewSet
    ```
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
    ```





    
 
