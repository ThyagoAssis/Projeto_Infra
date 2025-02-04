from django.contrib import admin
from .models import Ativo, TipoAtivo, Fabricante, Modelo

# Register your models here.
admin.site.register(Ativo),
admin.site.register(TipoAtivo),
admin.site.register(Fabricante),
admin.site.register(Modelo),

