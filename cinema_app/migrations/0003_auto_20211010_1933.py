# Generated by Django 3.2.7 on 2021-10-10 19:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0002_auto_20211010_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exibicao',
            name='data_hora',
        ),
        migrations.AddField(
            model_name='exibicao',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='exibicao',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
