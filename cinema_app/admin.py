from django.contrib import admin
from .models import Administrador, Exibicao, Filme,Artigo
# Register your models here.


admin.site.register(Filme)
admin.site.register(Exibicao)
admin.site.register(Artigo)
