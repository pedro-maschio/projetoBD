from django.contrib import admin
from .models import Administrador, Exibicao, Filme
# Register your models here.


admin.site.register(Administrador)
admin.site.register(Filme)
admin.site.register(Exibicao)