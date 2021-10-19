from django.db import models
from django.db.models.deletion import CASCADE
import django.utils.timezone

# Create your models here.

class Administrador(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=256)

    def __str__(self):
        return "{}, {}".format(self.nome, self.cpf)

class Filme(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField(   )
    nome_diretor = models.CharField(max_length=200)
    poster_img = models.CharField(max_length=200)
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