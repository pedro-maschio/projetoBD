# Generated by Django 3.2.7 on 2021-10-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_app', '0005_alter_filme_poster_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='audio',
        ),
        migrations.RemoveField(
            model_name='filme',
            name='legenda',
        ),
        migrations.AlterField(
            model_name='filme',
            name='poster_img',
            field=models.CharField(max_length=200),
        ),
    ]
