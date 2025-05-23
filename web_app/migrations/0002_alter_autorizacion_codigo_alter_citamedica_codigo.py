# Generated by Django 5.1.2 on 2025-04-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorizacion',
            name='codigo',
            field=models.CharField(max_length=50, unique=True, verbose_name='Código de la autorización de servicios'),
        ),
        migrations.AlterField(
            model_name='citamedica',
            name='codigo',
            field=models.CharField(blank=True, editable=False, max_length=50, unique=True, verbose_name='Código de la cita'),
        ),
    ]
