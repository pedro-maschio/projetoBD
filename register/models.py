from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Administrador(models.Model):
    user =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=25)

    class Meta:
        db_table = 'administrador' 

    def __str__(self):
        return str(self.user)

class Cliente(models.Model):
    user =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=25)

    class Meta:
        db_table = 'cliente' 

    def __str__(self):
        return str(self.user)
# class Cliente(models.Model):
#     user =  models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     email = models.EmailField()
#     cpf = models.CharField(max_length=15)
#     data_nascimento = models.DateTimeField()
#     sexos = [('Masc', 'Masculino'),('Fem','Feminino')]
#     sexo = models.CharField(choices = sexos)
#     vacinado = models.BooleanField()
#
#     def __str__(self):
#         return str(self.user)
