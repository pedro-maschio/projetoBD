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
    nome = models.CharField(max_length=200, verbose_name='Nome do filme')
    ano_lancamento = models.IntegerField(verbose_name='Ano de lançamento')
    nome_diretor = models.CharField(max_length=200, verbose_name='Nome do Diretor')
    poster_img = models.CharField(max_length=200, verbose_name='Imagem do pôster')
    duracao_min = models.IntegerField(verbose_name='Duração em minutos')
    elenco = models.CharField(max_length=100, verbose_name='Elenco Principal')
    genero = models.CharField(max_length=50, verbose_name='Gênero')
    sinopse = models.CharField(max_length=200, verbose_name='Sinopse')

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