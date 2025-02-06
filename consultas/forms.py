from django import forms
from ativos.models import Ativo

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = ['nome', 'tipo', 'fabricante', 'mac_address']

        labels = {
            'nome': 'Nome do Ativo:',
            'tipo': 'Tipo:',
            'fabricante': 'Fabricante:',
            'mac_address': 'Endereço MAC:',
        }

        widgets = {
                "nome": forms.TextInput(attrs={"class": "form-control"}),
                "tipo": forms.Select(attrs={"class": "form-control",}),
                "fabricante": forms.Select(attrs={"class": "form-control",}),
                "mac_address": forms.TextInput(attrs={"class": "form-control"}),
            }