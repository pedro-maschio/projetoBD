from django.contrib import admin
from .models import Administrador, Exibicao, Filme,Artigo,Cinema, Sala, Avaliacao
# Register your models here.


admin.site.register(Filme)
admin.site.register(Exibicao)
admin.site.register(Artigo)
admin.site.register(Cinema)
admin.site.register(Sala)
admin.site.register(Avaliacao)
