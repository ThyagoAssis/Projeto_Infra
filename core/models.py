from django.db import models

# Create your models here.
class Unidade(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="departamentos")

    def __str__(self):
        return f"{self.nome} - {self.unidade.nome}"