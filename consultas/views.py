from django.shortcuts import render
from ativos.models import Ativo
from .forms import ConsultaForm
# Create your views here.


def consultar_ativos(request):
    ativos = Ativo.objects.all()
    form = ConsultaForm()
    
    nome_id = request.GET.get('nome')
    unidade_id = request.GET.get('unidade')
    departamento_id = request.GET.get('departamento')
    tipo_id = request.GET.get('tipo')
    fabricante_id = request.GET.get('fabricante')
    ip = request.GET.get('ip')
    mac = request.GET.get('mac')

    if unidade_id:
        ativos = ativos.filter(unidade_id=unidade_id)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    elif departamento_id:
        ativos = ativos.filter(departamento_id=departamento_id)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    elif tipo_id:
        ativos = ativos.filter(tipo_id=tipo_id)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    elif fabricante_id:
        ativos = ativos.filter(fabricante_id=fabricante_id)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    elif ip:
        ativos = ativos.filter(ip=ip)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    elif mac:
        ativos = ativos.filter(mac_address__icontains=mac)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    elif mac:
        ativos = ativos.filter(nome_id=nome_id)
        return render(request, 'consultas/consulta.html', {'ativos': ativos})
    else: 
        return render(request, 'consultas/consulta.html', {'form':form})