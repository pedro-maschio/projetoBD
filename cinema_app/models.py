from django.db import models
from django.db.models.deletion import CASCADE
import django.utils.timezone
from register.models import Administrador

# Create your models here.

class Filme(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do filme")
    ano_lancamento = models.IntegerField(verbose_name="Ano de lançamento")
    nome_diretor = models.CharField(max_length=200, verbose_name="Nome do diretor")
    poster_img = models.ImageField(upload_to='images/', verbose_name="Imagem do filme")
    duracao_min = models.IntegerField(verbose_name="Duração em minutos")
    elenco = models.CharField(max_length=100, verbose_name="Elenco")
    genero = models.CharField(max_length=50, verbose_name="Genero")
    sinopse = models.CharField(max_length=200, verbose_name="Sinopse")

    def __str__(self):
        return "{}, {}".format(self.nome, self.ano_lancamento)

class Sala(models.Model):
    numero_assentos = models.IntegerField(default=0)

    def __str__(self):
        return "Código {}, {} assentos".format(self.id, self.numero_assentos)

class Exibicao(models.Model):
    codigo_filme = models.ForeignKey(Filme, models.SET_NULL, blank=True, null=True)
    codigo_sala = models.ForeignKey(Sala, models.SET_NULL, blank=True, null=True)
    #codigo_administrador = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True)
    audio = models.CharField(max_length=50, verbose_name="Áudio")
    legenda = models.CharField(max_length=50, verbose_name="Legenda")
    data = models.DateField(default=django.utils.timezone.now, verbose_name="Data de exibição")
    hora = models.TimeField(default=django.utils.timezone.now, verbose_name="Início da exibição")

    def __str__(self):
        return "{} {} {}".format(self.codigo_filme, self.data, self.hora)

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100, verbose_name="Título")
    texto = models.TextField()
    artigo_img = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True, verbose_name="Autor")
