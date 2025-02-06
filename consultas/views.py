from django.shortcuts import render
from ativos.models import Ativo
from .forms import ConsultaForm
# Create your views here.


def consultar_ativos(request):
    ativos = Ativo.objects.all()
    form = ConsultaForm()
    
    unidade_id = request.GET.get('unidade')
    departamento_id = request.GET.get('departamento')
    tipo_id = request.GET.get('tipo')
    fabricante_id = request.GET.get('fabricante')
    ip = request.GET.get('ip')
    mac = request.GET.get('mac')

    if unidade_id:
        ativos = ativos.filter(unidade_id=unidade_id)
    if departamento_id:
        ativos = ativos.filter(departamento_id=departamento_id)
    if tipo_id:
        ativos = ativos.filter(tipo_id=tipo_id)
    if fabricante_id:
        ativos = ativos.filter(fabricante_id=fabricante_id)
    if ip:
        ativos = ativos.filter(ip=ip)
    if mac:
        ativos = ativos.filter(mac_address__icontains=mac)


    return render(request, 'consultas/consulta.html', {'ativos': ativos, 'form': form})