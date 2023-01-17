# Generated by Django 4.1.5 on 2023-01-12 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignusers',
            name='dni_user',
            field=models.IntegerField(blank=True, null=True, verbose_name='Documento de Identidad'),
        ),
        migrations.AlterField(
            model_name='assignusers',
            name='email_user',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Correo corporativo'),
        ),
        migrations.AlterField(
            model_name='assignusers',
            name='name_user',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre completo'),
        ),
    ]