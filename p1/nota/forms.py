from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "nota1", "nota2"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder":"Nome"}),
            "nota1": forms.NumberInput(attrs={"step":"0.1", "min":"0", "max":"10"}),
            "nota2": forms.NumberInput(attrs={"step":"0.1", "min":"0", "max":"10"}),
        }
