from django.db import models

# Create your models here.
from core.models import Unidade, Departamento  # Importando os modelos do app core

class TipoAtivo(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Fabricante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, related_name="modelos")
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fabricante.nome} - {self.nome}"

class Ativo(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoAtivo, on_delete=models.SET_NULL, null=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.SET_NULL, null=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, related_name="ativos")
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    data_aquisicao = models.DateField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.modelo}) - {self.unidade.nome}"