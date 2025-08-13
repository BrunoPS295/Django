from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno

# Create your views here.
def criar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save()
            return redirect("nota:aluno_detail", pk=aluno.pk)
    else:
        form = AlunoForm()
    return render(request, "nota/criar_aluno.html", {"form": form})

def listar_alunos(request):
    alunos = Aluno.objects.all().order_by("-id")
    return render(request, "nota/listar_alunos.html", {"alunos": alunos})