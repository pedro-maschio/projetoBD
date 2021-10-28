from django.db import models
from django.db.models.deletion import CASCADE
import django.utils.timezone
from register.models import Administrador, Cliente
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from .assento_padroes import CINEMA

# Create your models here.

class Filme(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do filme")
    ano_lancamento = models.IntegerField(verbose_name="Ano de lançamento")
    nome_diretor = models.CharField(max_length=200, verbose_name="Nome do diretor")
    poster_img = models.ImageField(upload_to='images/', verbose_name="Imagem do filme")
    poster_img_blob = models.BinaryField()
    duracao_min = models.IntegerField(verbose_name="Duração em minutos")
    elenco = models.CharField(max_length=100, verbose_name="Elenco")
    genero = models.CharField(max_length=50, verbose_name="Genero")
    sinopse = models.CharField(max_length=200, verbose_name="Sinopse")

    class Meta:
        db_table = 'filme' 

    def __str__(self):
        return "{} ({})".format(self.nome, self.ano_lancamento)



class Cinema(models.Model):
    cnpj = models.CharField(max_length = 18, verbose_name="CNPJ")
    nome = models.CharField(max_length=50, verbose_name="Nome do cinema")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    cep = models.CharField(max_length=20, verbose_name="CEP")
    numero = models.CharField(max_length = 20, verbose_name="Telefone")
    cidade = models.CharField(max_length=50, verbose_name="Cidade")
    estado = models.CharField(max_length=50, verbose_name="Estado")
    codigo_admin = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True, verbose_name="Administrador")

    class Meta:
        db_table = 'cinema' 

    def __str__(self):
        return " {} - {} ".format(self.nome, self.cidade)

class Sala(models.Model):
    numero_assentos = models.IntegerField(default=0, verbose_name="Número de assentos")
    codigo_cinema = models.ForeignKey(Cinema, models.SET_NULL, blank=True, null=True, verbose_name="Sala")
    sessao_3d = models.BooleanField(verbose_name="Sessão em 3D")
    sessao_normal = models.BooleanField(verbose_name="Sessão Normal")
    sessao_platinum = models.BooleanField(verbose_name="Sessão Platinum")

    class Meta:
        db_table = 'sala' 

    def __str__(self):
        return "Código {} - com {} assentos".format(self.id, self.numero_assentos)

class Exibicao(models.Model):
    codigo_filme = models.ForeignKey(Filme, models.SET_NULL, blank=True, null=True, verbose_name="Filme")
    codigo_sala = models.ForeignKey(Sala, models.SET_NULL, blank=True, null=True, verbose_name="Sala")
    codigo_cinema = models.ForeignKey(Cinema, models.SET_NULL, blank=True, null=True, verbose_name="Cinema")
    #codigo_administrador = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True)
    audio = models.CharField(max_length=50, verbose_name="Áudio")
    legenda = models.CharField(max_length=50, verbose_name="Legenda")
    data = models.DateField(default=django.utils.timezone.now, verbose_name="Data de exibição")
    hora = models.TimeField(default=django.utils.timezone.now, verbose_name="Início da exibição")

    class Meta:
        db_table = 'exibicao' 

    def __str__(self):
        return "{} {} {}".format(self.codigo_filme, self.data, self.hora)

class Artigo(models.Model):
    titulo = models.CharField(max_length = 100, verbose_name="Título")
    texto = models.TextField(verbose_name="Texto")
    artigo_img = models.ImageField(upload_to='images/')
    author = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True, verbose_name="Autor")

    class Meta:
        db_table = 'artigo' 


class Reserva(models.Model):
    codigo_exibicao = models.ForeignKey(Exibicao, models.SET_NULL, blank=True, null=True, verbose_name="Exibição")
    codigo_cliente = models.ForeignKey(Cliente, models.SET_NULL, blank=True, null=True, verbose_name="Cliente")
    codigo_administrador = models.ForeignKey(Administrador, models.SET_NULL, blank=True, null=True, verbose_name="Administrador")
    data = models.DateField(default=django.utils.timezone.now, verbose_name="Data da reserva")
    hora = models.TimeField(default=django.utils.timezone.now, verbose_name="Horário da reserva")

    class Meta:
        db_table = 'reserva' 

class Avaliacao(models.Model):
    nota = models.IntegerField(default=0, validators=[MaxValueValidator(5),MinValueValidator(0),], verbose_name="Nota")
    comentario = models.TextField(verbose_name="Comentário")
    codigo_filme = models.ForeignKey(Filme, models.SET_NULL, blank=True, null=True, verbose_name="Filme")
    codigo_cliente = models.ForeignKey(Cliente, models.SET_NULL, blank=True, null=True, verbose_name="Cliente")

    class Meta:
        db_table = 'avaliacao' 

class Assento(models.Model):
    fileira = models.IntegerField()
    numero = models.IntegerField()
    adaptado = models.BooleanField(verbose_name="Adaptado")
    estado_conservacao = models.CharField(max_length = 100, verbose_name="Conservação")
    codigo_cliente = models.ForeignKey(Cliente, models.SET_NULL, blank=True, null=True, verbose_name="Reservado")
    codigo_sala = models.ForeignKey(Sala, models.SET_NULL, blank=True, null=True, verbose_name="Sala")

    class Meta:
        db_table = 'assento' 
    

@receiver(post_save, sender=Sala)
def criar_assento(sender, instance, created, **kwargs):
    if created:
        for row, assentos in enumerate(CINEMA):
            for col, assento in enumerate(assentos):
                if assento==2:
                    Assento.objects.create(codigo_sala=instance, estado_conservacao="bom", fileira=row, numero=col, adaptado=True)
                elif assento:
                    Assento.objects.create(codigo_sala=instance, estado_conservacao="bom", fileira=row, numero=col, adaptado=False)

       




# def criar_avaliacao(sender, instance, created, **kwargs):
#     if created:
#         Assento.objects.create(codigo_cliente=instance)
#     post_save.connect(criar_assento, sender=Sala) 


 #   status = models.CharField(max_length=20, choices=(('available', 'available'), ('reserved', 'reserved'), ('unavailable', 'unavailable'),), default='Available')

  
