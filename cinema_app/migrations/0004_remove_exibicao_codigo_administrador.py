# Generated by Django 3.2.7 on 2021-10-15 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0003_auto_20211010_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exibicao',
            name='codigo_administrador',
        ),
    ]