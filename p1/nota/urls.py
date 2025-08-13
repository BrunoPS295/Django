from django.urls import path
from . import views

app_name = "nota"

urlpatterns = [
    path("", views.listar_alunos, name="listar_alunos"),
    path("novo/", views.criar_aluno, name="criar_aluno"),
]
