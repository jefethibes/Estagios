from django.urls import path

from controle_estagios.views import cursos, estagios, empresas, alunos, index

app_name = 'controle_estagios'

urlpatterns = [
    path('form_cursos/', cursos.AddCursos.as_view(), name='form_cursos'),
    path('list_cursos/', cursos.ListCursos.as_view(), name='list_cursos'),
    path('update_cursos/<int:pk>/', cursos.UpdateCursos.as_view(), name='update_cursos'),
    path('form_estagios/', estagios.AddEstagios.as_view(), name='form_estagios'),
    path('list_estagios/', estagios.ListEstagios.as_view(), name='list_estagios'),
    path('update_estagios/<int:pk>/', estagios.UpdateEstagios.as_view(), name='update_estagios'),
    path('form_empresas/', empresas.AddEmpresas.as_view(), name='form_empresas'),
    path('list_empresas/', empresas.ListEmpresas.as_view(), name='list_empresas'),
    path('update_empresas/<int:pk>/', empresas.UpdateEmpresas.as_view(), name='update_empresas'),
    path('form_alunos/', alunos.AddAlunos.as_view(), name='form_alunos'),
    path('list_alunos/', alunos.ListAlunos.as_view(), name='list_alunos'),
    path('update_alunos/<int:pk>/', alunos.UpdateAlunos.as_view(), name='update_alunos'),
    path('', index.index, name='index'),
]
