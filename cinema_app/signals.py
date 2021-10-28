from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Assento, Sala
from .assento_padroes import CINEMA

def criar_assento(sender, instance, created, **kwargs):
    print("chamou")
    if created:
        for row, assentos in enumerate(CINEMA):
            for col, assento in enumerate(assentos):
                if assento==2:
                    Assento.objects.create(codigo_sala=instance, estado_conservacao="Novo", fileira=row, numero=col, adaptado=True)
                elif assento:
                    Assento.objects.create(codigo_sala=instance, estado_conservacao="Novo", fileira=row, numero=col, adaptado=False)
    post_save.connect(criar_assento, sender=Sala) 