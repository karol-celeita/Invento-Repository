# Generated by Django 4.1 on 2023-01-19 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actives', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('name_user', models.CharField(max_length=150, verbose_name='Nombre completo')),
                ('email_user', models.CharField(max_length=150, verbose_name='Correo corporativo')),
                ('dni_user', models.IntegerField(verbose_name='Documento de Identidad')),
                ('type_assignment', models.CharField(choices=[('Contrato fijo', 'Contrato fijo'), ('Contrato indefinido', 'Contrato indefinido'), ('Prestamo', 'Prestamo'), ('Fijo al area', 'Fijo al area'), ('Aprendiz', 'Aprendiz'), ('Practicante', 'Practicante'), ('Contrato prestacion', 'Contrato prestacion'), ('Por definir', 'Por definir')], default='Por definir', max_length=20, verbose_name='Tipo asignación')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='AssignUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('date_assignment', models.DateField(verbose_name='Fecha de asignación')),
                ('type_assignment', models.CharField(choices=[('Contrato fijo', 'Contrato fijo'), ('Contrato indefinido', 'Contrato indefinido'), ('Prestamo', 'Prestamo'), ('Fijo al area', 'Fijo al area'), ('Aprendiz', 'Aprendiz'), ('Practicante', 'Practicante'), ('Contrato prestacion', 'Contrato prestacion'), ('Por definir', 'Por definir')], default='Por definir', max_length=20, verbose_name='Tipo asignación')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.userdata', verbose_name='Encargado')),
                ('computers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actives.computers', verbose_name='Equipo asignado')),
                ('passive_devices', models.ManyToManyField(to='actives.passivedevices', verbose_name='Dispositivos asignados')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Encargado')),
            ],
            options={
                'verbose_name': 'Asignación Usuario',
                'verbose_name_plural': 'Asignación Usuarios',
            },
        ),
    ]
