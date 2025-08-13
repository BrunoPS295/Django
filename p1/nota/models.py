from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
# Create your models here.

class Aluno(models.Model):
    nome = models.CharField("Nome", max_length=100)
    nota1 = models.DecimalField(
        "Nota 1",
        max_digits=4, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.0')), MaxValueValidator(Decimal('10.0'))],
        default=Decimal('0.0'),
    )
    nota2 = models.DecimalField(
        "Nota 2",
        max_digits=4, decimal_places=2,
        validators=[MinValueValidator(Decimal('0.0')), MaxValueValidator(Decimal('10.0'))],
        default=Decimal('0.0'),
    )

    def __str__(self):
        return f"{self.nome} ({self.nota1}, {self.nota2})"

    @property
    def media(self):
        return (Decimal(self.nota1) + Decimal(self.nota2)) / 2
