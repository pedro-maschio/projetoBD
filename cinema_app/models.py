from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Administrador(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=256)

    def __str__(self):
        return "{} {} {} {}".format(self.nome, self.cpf, self.email, self.senha)

class Filme(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField(   )
    nome_diretor = models.CharField(max_length=200)
    audio = models.CharField(max_length=50)
    legenda = models.CharField(max_length=50)
    poster_img = models.CharField(max_length=200)
    duracao_min = models.IntegerField()
    elenco = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    sinopse = models.CharField(max_length=200)

    def __str__(self):
        return "{} {} {}".format(self.nome, self.ano_lancamento, self.nome_diretor)

class Sala(models.Model):
    numero_assentos = models.IntegerField
    saida_emergencia = models.BooleanField

class Exibicao(models.Model):
    codigo_filme = models.ForeignKey(Filme, models.SET_NULL, blank=True, null=True)
    codigo_sala = models.ForeignKey(Sala, models.SET_NULL, blank=True, null=True)
    codigo_administrador = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True)
    data_hora = models.DateTimeField()

    def __str__(self):
        return "{} {} {}".format(self.codigo_filme, self.codigo_administrador, self.data_hora)