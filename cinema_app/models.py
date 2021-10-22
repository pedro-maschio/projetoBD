from django.db import models
from django.db.models.deletion import CASCADE
import django.utils.timezone
from register.models import Administrador

# Create your models here.

class Filme(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField(   )
    nome_diretor = models.CharField(max_length=200)
    audio = models.CharField(max_length=50)
    legenda = models.CharField(max_length=50)
    poster_img = models.ImageField(upload_to='images/')
    duracao_min = models.IntegerField()
    elenco = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopse = models.CharField(max_length=200)

    def __str__(self):
        return "{}, {}".format(self.nome, self.ano_lancamento)

class Sala(models.Model):
    numero_assentos = models.IntegerField(default=0)
    saida_emergencia = models.BooleanField()

    def __str__(self):
        return "Código {}, {} assentos".format(self.id, self.numero_assentos)

class Exibicao(models.Model):
    codigo_filme = models.ForeignKey(Filme, models.SET_NULL, blank=True, null=True)
    codigo_sala = models.ForeignKey(Sala, models.SET_NULL, blank=True, null=True)
    #codigo_administrador = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True)
    data = models.DateField(default=django.utils.timezone.now)
    hora = models.TimeField(default=django.utils.timezone.now)

    def __str__(self):
        return "{} {} {}".format(self.codigo_filme, self.data, self.hora)

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100)
    texto = models.TextField()
    artigo_img = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True)
